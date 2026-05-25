-- QC release workflow for inventory stock.
-- Previously there was no mechanism to move stock out of Quarantine —
-- this adds the audit table, status constraint, and two RPC functions.

-- 1. Status constraint on inventory_stock
ALTER TABLE inventory_stock
  ADD CONSTRAINT inventory_stock_status_check
  CHECK (status = ANY (ARRAY[
    'Quarantine',   -- newly received, pending QC
    'Available',    -- QC approved, ready to use
    'Depleted',     -- fully consumed
    'Rejected',     -- failed QC
    'Expired'       -- past expiry date
  ]));

-- 2. QC release audit table
CREATE TABLE IF NOT EXISTS stock_qc_releases (
  id            uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  stock_id      uuid NOT NULL REFERENCES inventory_stock(id) ON DELETE CASCADE,
  action        text NOT NULL CHECK (action IN ('Released', 'Rejected')),
  actioned_by   uuid NOT NULL REFERENCES employees(id),
  actioned_at   timestamptz NOT NULL DEFAULT now(),
  notes         text,
  previous_status text NOT NULL
);

CREATE INDEX idx_stock_qc_releases_stock_id    ON stock_qc_releases(stock_id);
CREATE INDEX idx_stock_qc_releases_actioned_by ON stock_qc_releases(actioned_by);

ALTER TABLE stock_qc_releases ENABLE ROW LEVEL SECURITY;

CREATE POLICY "stock_qc_releases_select"
  ON stock_qc_releases FOR SELECT TO authenticated USING (true);

CREATE POLICY "stock_qc_releases_insert"
  ON stock_qc_releases FOR INSERT TO authenticated
  WITH CHECK (auth.role() = 'authenticated');

-- 3. Release: Quarantine → Available
CREATE OR REPLACE FUNCTION release_stock_from_quarantine(
  p_stock_id uuid,
  p_notes    text DEFAULT NULL
)
RETURNS jsonb
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = public, pg_temp
AS $$
DECLARE
  v_stock     inventory_stock%ROWTYPE;
  v_emp_id    uuid;
  v_item_name text;
BEGIN
  SELECT * INTO v_stock FROM inventory_stock WHERE id = p_stock_id FOR UPDATE;

  IF NOT FOUND THEN
    RAISE EXCEPTION 'Stock record not found: %', p_stock_id;
  END IF;

  IF v_stock.status != 'Quarantine' THEN
    RAISE EXCEPTION 'Stock is not in Quarantine. Current status: %', v_stock.status;
  END IF;

  SELECT id INTO v_emp_id FROM employees
  WHERE email = auth.jwt()->>'email' AND is_active = true;

  IF v_emp_id IS NULL THEN
    RAISE EXCEPTION 'Authenticated user not found in employees table';
  END IF;

  SELECT name INTO v_item_name FROM inventory_items WHERE id = v_stock.item_id;

  UPDATE inventory_stock SET status = 'Available' WHERE id = p_stock_id;

  INSERT INTO stock_qc_releases (stock_id, action, actioned_by, notes, previous_status)
  VALUES (p_stock_id, 'Released', v_emp_id, p_notes, 'Quarantine');

  INSERT INTO inventory_movements (stock_id, type, quantity, purpose, notes, issued_by)
  VALUES (p_stock_id, 'qc_release', 0, 'QC Release',
    coalesce(p_notes, 'Released from Quarantine to Available'), v_emp_id);

  RETURN jsonb_build_object(
    'success', true,
    'stock_id', p_stock_id,
    'item_name', v_item_name,
    'status', 'Available'
  );
END;
$$;

GRANT EXECUTE ON FUNCTION release_stock_from_quarantine(uuid, text) TO authenticated;

-- 4. Reject: Quarantine → Rejected
CREATE OR REPLACE FUNCTION reject_quarantine_stock(
  p_stock_id uuid,
  p_reason   text
)
RETURNS jsonb
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = public, pg_temp
AS $$
DECLARE
  v_stock     inventory_stock%ROWTYPE;
  v_emp_id    uuid;
  v_item_name text;
BEGIN
  SELECT * INTO v_stock FROM inventory_stock WHERE id = p_stock_id FOR UPDATE;

  IF NOT FOUND THEN
    RAISE EXCEPTION 'Stock record not found: %', p_stock_id;
  END IF;

  IF v_stock.status != 'Quarantine' THEN
    RAISE EXCEPTION 'Stock is not in Quarantine. Current status: %', v_stock.status;
  END IF;

  IF p_reason IS NULL OR trim(p_reason) = '' THEN
    RAISE EXCEPTION 'A rejection reason is required';
  END IF;

  SELECT id INTO v_emp_id FROM employees
  WHERE email = auth.jwt()->>'email' AND is_active = true;

  IF v_emp_id IS NULL THEN
    RAISE EXCEPTION 'Authenticated user not found in employees table';
  END IF;

  SELECT name INTO v_item_name FROM inventory_items WHERE id = v_stock.item_id;

  UPDATE inventory_stock SET status = 'Rejected' WHERE id = p_stock_id;

  INSERT INTO stock_qc_releases (stock_id, action, actioned_by, notes, previous_status)
  VALUES (p_stock_id, 'Rejected', v_emp_id, p_reason, 'Quarantine');

  INSERT INTO inventory_movements (stock_id, type, quantity, purpose, notes, issued_by)
  VALUES (p_stock_id, 'qc_rejection', 0, 'QC Rejection', p_reason, v_emp_id);

  RETURN jsonb_build_object(
    'success', true,
    'stock_id', p_stock_id,
    'item_name', v_item_name,
    'status', 'Rejected',
    'reason', p_reason
  );
END;
$$;

GRANT EXECUTE ON FUNCTION reject_quarantine_stock(uuid, text) TO authenticated;
