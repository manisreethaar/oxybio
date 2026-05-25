-- Versioning: when editing an Approved recipe, archive the old record and create
-- a new Draft with version+1 and base_version_id linking back to the original.
-- Call via: supabase.rpc('create_formulation_revision', { p_id: <uuid> })
CREATE OR REPLACE FUNCTION create_formulation_revision(p_id uuid)
RETURNS uuid
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = public, pg_temp
AS $$
DECLARE
  v_old formulations%ROWTYPE;
  v_new_id uuid;
BEGIN
  SELECT * INTO v_old FROM formulations WHERE id = p_id FOR UPDATE;

  IF NOT FOUND THEN
    RAISE EXCEPTION 'Formulation not found: %', p_id;
  END IF;

  IF v_old.status != 'Approved' THEN
    RAISE EXCEPTION 'Only Approved formulations can be revised. Current status: %', v_old.status;
  END IF;

  UPDATE formulations SET status = 'Archived' WHERE id = p_id;

  INSERT INTO formulations (
    code, name, ingredients, notes, version,
    created_at, created_by, base_version_id,
    status, steps, approved_by, approved_at, rejection_reason
  ) VALUES (
    v_old.code, v_old.name, v_old.ingredients, v_old.notes,
    v_old.version + 1,
    now(), auth.uid(), p_id,
    'Draft', v_old.steps,
    NULL, NULL, NULL
  )
  RETURNING id INTO v_new_id;

  RETURN v_new_id;
END;
$$;

GRANT EXECUTE ON FUNCTION create_formulation_revision(uuid) TO authenticated;
