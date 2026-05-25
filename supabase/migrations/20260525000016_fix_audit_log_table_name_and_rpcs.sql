-- The reading_audit_log table pre-existed without a DEFAULT on table_name,
-- causing NOT NULL violation when the column was omitted from INSERT.
-- Fix: add DEFAULT retroactively + pass table_name explicitly in both RPCs.

ALTER TABLE reading_audit_log
  ALTER COLUMN table_name SET DEFAULT 'batch_fermentation_readings';

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
  SELECT id INTO v_admin_id FROM employees
  WHERE email = auth.jwt()->>'email' AND is_active = true LIMIT 1;

  IF v_admin_id IS NULL THEN RAISE EXCEPTION 'Not authenticated'; END IF;
  IF NOT is_admin() THEN RAISE EXCEPTION 'Admin access required'; END IF;

  SELECT * INTO v_old FROM batch_fermentation_readings WHERE id = p_reading_id FOR UPDATE;
  IF NOT FOUND THEN RAISE EXCEPTION 'Reading % not found', p_reading_id; END IF;

  INSERT INTO reading_audit_log(table_name, reading_id, action, changed_by, old_values, reason)
  VALUES ('batch_fermentation_readings', p_reading_id, 'UPDATE', v_admin_id, to_jsonb(v_old), p_reason);

  UPDATE batch_fermentation_readings SET
    ph               = COALESCE((p_updates->>'ph')::numeric,               ph),
    incubator_temp_c = COALESCE((p_updates->>'incubator_temp_c')::numeric, incubator_temp_c),
    brix             = COALESCE((p_updates->>'brix')::numeric,             brix),
    optical_density  = COALESCE((p_updates->>'optical_density')::numeric,  optical_density),
    elapsed_hours    = COALESCE((p_updates->>'elapsed_hours')::numeric,    elapsed_hours),
    logged_at        = COALESCE((p_updates->>'logged_at')::timestamptz,    logged_at),
    is_retrospective = COALESCE((p_updates->>'is_retrospective')::boolean, is_retrospective),
    retro_reason     = COALESCE(p_updates->>'retro_reason',                retro_reason),
    foam_level       = COALESCE(p_updates->>'foam_level',                  foam_level),
    visual_appearance= COALESCE(p_updates->>'visual_appearance',           visual_appearance),
    plating_result   = COALESCE(p_updates->>'plating_result',              plating_result),
    notes            = COALESCE(p_updates->>'notes',                       notes),
    updated_at       = now(),
    updated_by       = v_admin_id,
    edit_reason      = p_reason
  WHERE id = p_reading_id;

  RETURN jsonb_build_object('success', true, 'reading_id', p_reading_id);
END;
$$;

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

  IF v_admin_id IS NULL THEN RAISE EXCEPTION 'Not authenticated'; END IF;
  IF NOT is_admin() THEN RAISE EXCEPTION 'Admin access required'; END IF;

  SELECT * INTO v_old FROM batch_fermentation_readings WHERE id = p_reading_id FOR UPDATE;
  IF NOT FOUND THEN RAISE EXCEPTION 'Reading % not found', p_reading_id; END IF;

  INSERT INTO reading_audit_log(table_name, reading_id, action, changed_by, old_values, reason)
  VALUES ('batch_fermentation_readings', p_reading_id, 'DELETE', v_admin_id, to_jsonb(v_old), p_reason);

  DELETE FROM batch_fermentation_readings WHERE id = p_reading_id;

  RETURN jsonb_build_object('success', true, 'reading_id', p_reading_id);
END;
$$;

GRANT EXECUTE ON FUNCTION update_fermentation_reading(uuid, jsonb, text) TO authenticated;
GRANT EXECUTE ON FUNCTION delete_fermentation_reading(uuid, text) TO authenticated;
