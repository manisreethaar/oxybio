-- Audit trail + tightened RLS for batch_fermentation_readings.
-- Adds updated_at/updated_by/edit_reason tracking columns,
-- a reading_audit_log table, and two admin-only RPCs for
-- editing and deleting readings with full audit trail.

-- 1. Tracking columns on batch_fermentation_readings
ALTER TABLE batch_fermentation_readings
  ADD COLUMN IF NOT EXISTS updated_at   timestamptz,
  ADD COLUMN IF NOT EXISTS updated_by   uuid REFERENCES employees(id) ON DELETE SET NULL,
  ADD COLUMN IF NOT EXISTS edit_reason  text;

-- 2. Audit log table
CREATE TABLE IF NOT EXISTS reading_audit_log (
  id          uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  table_name  text NOT NULL DEFAULT 'batch_fermentation_readings',
  reading_id  uuid NOT NULL,
  action      text NOT NULL CHECK (action IN ('UPDATE','DELETE')),
  changed_by  uuid REFERENCES employees(id) ON DELETE SET NULL,
  changed_at  timestamptz NOT NULL DEFAULT now(),
  old_values  jsonb,
  reason      text
);

CREATE INDEX IF NOT EXISTS idx_reading_audit_reading_id ON reading_audit_log(reading_id);
CREATE INDEX IF NOT EXISTS idx_reading_audit_changed_at  ON reading_audit_log(changed_at DESC);

-- 3. RLS: replace catch-all policy with split SELECT/INSERT/UPDATE/DELETE
ALTER TABLE batch_fermentation_readings ENABLE ROW LEVEL SECURITY;

DROP POLICY IF EXISTS bfr_auth_all  ON batch_fermentation_readings;
DROP POLICY IF EXISTS bfr_select    ON batch_fermentation_readings;
DROP POLICY IF EXISTS bfr_insert    ON batch_fermentation_readings;
DROP POLICY IF EXISTS bfr_update    ON batch_fermentation_readings;
DROP POLICY IF EXISTS bfr_delete    ON batch_fermentation_readings;

CREATE POLICY bfr_select ON batch_fermentation_readings
  FOR SELECT TO authenticated USING (true);

CREATE POLICY bfr_insert ON batch_fermentation_readings
  FOR INSERT TO authenticated WITH CHECK (true);

CREATE POLICY bfr_update ON batch_fermentation_readings
  FOR UPDATE TO authenticated
  USING (
    logged_by = (SELECT id FROM employees WHERE email = auth.jwt()->>'email' LIMIT 1)
    OR is_admin()
  );

CREATE POLICY bfr_delete ON batch_fermentation_readings
  FOR DELETE TO authenticated USING (is_admin());

-- 4. update_fermentation_reading — admin only, full audit
CREATE OR REPLACE FUNCTION update_fermentation_reading(
  p_reading_id uuid,
  p_updates    jsonb,
  p_reason     text DEFAULT NULL
)
RETURNS jsonb
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = public, pg_temp
AS $$
DECLARE
  v_admin_id uuid;
  v_old      batch_fermentation_readings;
BEGIN
  -- resolve caller
  SELECT id INTO v_admin_id FROM employees
  WHERE email = auth.jwt()->>'email' AND is_active = true LIMIT 1;

  IF v_admin_id IS NULL THEN
    RAISE EXCEPTION 'Not authenticated';
  END IF;

  IF NOT is_admin() THEN
    RAISE EXCEPTION 'Admin access required';
  END IF;

  -- snapshot old row
  SELECT * INTO v_old FROM batch_fermentation_readings WHERE id = p_reading_id FOR UPDATE;
  IF NOT FOUND THEN
    RAISE EXCEPTION 'Reading % not found', p_reading_id;
  END IF;

  -- archive old values
  INSERT INTO reading_audit_log(reading_id, action, changed_by, old_values, reason)
  VALUES (
    p_reading_id, 'UPDATE', v_admin_id,
    to_jsonb(v_old),
    p_reason
  );

  -- apply COALESCE updates
  UPDATE batch_fermentation_readings SET
    ph               = COALESCE((p_updates->>'ph')::numeric,          ph),
    temperature      = COALESCE((p_updates->>'temperature')::numeric, temperature),
    brix             = COALESCE((p_updates->>'brix')::numeric,        brix),
    od_reading       = COALESCE((p_updates->>'od_reading')::numeric,  od_reading),
    elapsed_hours    = COALESCE((p_updates->>'elapsed_hours')::numeric, elapsed_hours),
    logged_at        = COALESCE((p_updates->>'logged_at')::timestamptz, logged_at),
    is_retrospective = COALESCE((p_updates->>'is_retrospective')::boolean, is_retrospective),
    retro_reason     = COALESCE(p_updates->>'retro_reason',           retro_reason),
    foam_level       = COALESCE(p_updates->>'foam_level',             foam_level),
    visual_notes     = COALESCE(p_updates->>'visual_notes',           visual_notes),
    notes            = COALESCE(p_updates->>'notes',                  notes),
    updated_at       = now(),
    updated_by       = v_admin_id,
    edit_reason      = p_reason
  WHERE id = p_reading_id;

  RETURN jsonb_build_object('success', true, 'reading_id', p_reading_id);
END;
$$;

GRANT EXECUTE ON FUNCTION update_fermentation_reading(uuid, jsonb, text) TO authenticated;

-- 5. delete_fermentation_reading — admin only, full audit
CREATE OR REPLACE FUNCTION delete_fermentation_reading(
  p_reading_id uuid,
  p_reason     text DEFAULT NULL
)
RETURNS jsonb
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = public, pg_temp
AS $$
DECLARE
  v_admin_id uuid;
  v_old      batch_fermentation_readings;
BEGIN
  SELECT id INTO v_admin_id FROM employees
  WHERE email = auth.jwt()->>'email' AND is_active = true LIMIT 1;

  IF v_admin_id IS NULL THEN
    RAISE EXCEPTION 'Not authenticated';
  END IF;

  IF NOT is_admin() THEN
    RAISE EXCEPTION 'Admin access required';
  END IF;

  SELECT * INTO v_old FROM batch_fermentation_readings WHERE id = p_reading_id FOR UPDATE;
  IF NOT FOUND THEN
    RAISE EXCEPTION 'Reading % not found', p_reading_id;
  END IF;

  INSERT INTO reading_audit_log(reading_id, action, changed_by, old_values, reason)
  VALUES (
    p_reading_id, 'DELETE', v_admin_id,
    to_jsonb(v_old),
    p_reason
  );

  DELETE FROM batch_fermentation_readings WHERE id = p_reading_id;

  RETURN jsonb_build_object('success', true, 'reading_id', p_reading_id);
END;
$$;

GRANT EXECUTE ON FUNCTION delete_fermentation_reading(uuid, text) TO authenticated;
