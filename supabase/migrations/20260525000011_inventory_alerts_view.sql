-- inventory_dashboard: unified view of all stock with health status flags.
-- inventory_alerts: filtered view showing only items needing attention.
-- Use inventory_alerts on the Inventory Hub home screen for at-a-glance status.

CREATE OR REPLACE VIEW inventory_dashboard AS
SELECT
  s.id                      AS stock_id,
  i.id                      AS item_id,
  i.item_code,
  i.name                    AS item_name,
  i.category,
  i.unit,
  s.supplier_batch_number   AS lot_number,
  s.current_quantity,
  s.received_quantity,
  i.min_stock_level,
  s.status,
  s.expiry_date,
  s.location,
  v.name                    AS vendor_name,
  s.created_at              AS received_at,

  CASE
    WHEN s.expiry_date IS NOT NULL
    THEN (s.expiry_date - CURRENT_DATE)
    ELSE NULL
  END AS days_to_expiry,

  CASE
    WHEN s.status = 'Depleted'                                          THEN 'out_of_stock'
    WHEN s.expiry_date IS NOT NULL AND s.expiry_date <= CURRENT_DATE    THEN 'expired'
    WHEN s.expiry_date IS NOT NULL
      AND s.expiry_date <= CURRENT_DATE + INTERVAL '30 days'            THEN 'expiring_soon'
    WHEN s.status = 'Available'
      AND i.min_stock_level > 0
      AND s.current_quantity <= i.min_stock_level                       THEN 'low_stock'
    WHEN s.status = 'Quarantine'                                        THEN 'pending_qc'
    WHEN s.status = 'Rejected'                                          THEN 'rejected'
    ELSE 'ok'
  END AS health_status

FROM inventory_stock s
JOIN inventory_items i ON i.id = s.item_id
LEFT JOIN vendors v ON v.id = s.vendor_id;

CREATE OR REPLACE VIEW inventory_alerts AS
SELECT * FROM inventory_dashboard
WHERE health_status IN ('out_of_stock','expired','expiring_soon','low_stock','pending_qc')
ORDER BY
  CASE health_status
    WHEN 'out_of_stock'   THEN 1
    WHEN 'expired'        THEN 2
    WHEN 'expiring_soon'  THEN 3
    WHEN 'low_stock'      THEN 4
    WHEN 'pending_qc'     THEN 5
  END,
  days_to_expiry ASC NULLS LAST;
