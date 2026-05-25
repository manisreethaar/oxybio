-- 1. Lot dropdown view: only consumable categories (Raw Materials, Chemicals,
--    Microbiological Media) that are Available and not expired.
--    Frontend should query this instead of raw inventory_stock so glassware
--    and lab consumables never appear in ingredient selectors.
CREATE OR REPLACE VIEW inventory_stock_consumables AS
SELECT
  s.id           AS stock_id,
  s.item_id,
  i.name         AS item_name,
  i.category,
  i.unit,
  s.supplier_batch_number AS lot_number,
  s.current_quantity,
  s.status,
  s.expiry_date,
  v.name         AS vendor_name
FROM inventory_stock s
JOIN inventory_items i ON i.id = s.item_id
LEFT JOIN vendors v ON v.id = s.vendor_id
WHERE i.category IN ('Raw Materials', 'Chemicals', 'Microbiological Media')
  AND s.status = 'Available'
  AND (s.expiry_date IS NULL OR s.expiry_date > CURRENT_DATE);

-- 2. Helper: calculate T+ elapsed hours for a batch reading.
--    Pass the actual reading timestamp (past or present) to get correct T+ value.
--    Frontend usage:
--      Normal:       get_elapsed_hours(batch_id)            → T+ from now
--      Retrospective: get_elapsed_hours(batch_id, '2026-05-02T10:00:00Z') → T+ from that time
CREATE OR REPLACE FUNCTION get_elapsed_hours(p_batch_id uuid, p_reading_time timestamptz DEFAULT now())
RETURNS numeric
LANGUAGE sql
STABLE
SECURITY DEFINER
SET search_path = public, pg_temp
AS $$
  SELECT ROUND(
    EXTRACT(EPOCH FROM (p_reading_time - b.start_time)) / 3600.0,
    2
  )
  FROM batches b WHERE b.id = p_batch_id;
$$;

GRANT EXECUTE ON FUNCTION get_elapsed_hours(uuid, timestamptz) TO authenticated;
