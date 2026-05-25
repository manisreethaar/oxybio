-- Single function to retrieve all data for a batch across every module.
-- Returns a JSONB object with every related record grouped by module.
-- Frontend usage: supabase.rpc('get_batch_overview', { p_batch_id: '<uuid>' })
CREATE OR REPLACE FUNCTION get_batch_overview(p_batch_id uuid)
RETURNS jsonb
LANGUAGE plpgsql
STABLE
SECURITY DEFINER
SET search_path = public, pg_temp
AS $$
DECLARE
  v_batch batches%ROWTYPE;
  v_result jsonb;
BEGIN
  SELECT * INTO v_batch FROM batches WHERE id = p_batch_id;

  IF NOT FOUND THEN
    RAISE EXCEPTION 'Batch not found: %', p_batch_id;
  END IF;

  SELECT jsonb_build_object(

    -- Core batch record + linked recipe
    'batch', to_jsonb(v_batch),

    'formulation', (
      SELECT to_jsonb(f) FROM formulations f WHERE f.id = v_batch.formulation_id
    ),

    -- Process stages
    'stages', jsonb_build_object(
      'media_prep', (
        SELECT COALESCE(jsonb_agg(s ORDER BY s.created_at), '[]')
        FROM batch_stage_media_prep s WHERE s.batch_id = p_batch_id
      ),
      'sterilisation', (
        SELECT COALESCE(jsonb_agg(s ORDER BY s.created_at), '[]')
        FROM batch_stage_sterilisation s WHERE s.batch_id = p_batch_id
      ),
      'harvest', (
        SELECT COALESCE(jsonb_agg(s ORDER BY s.created_at), '[]')
        FROM batch_stage_harvest s WHERE s.batch_id = p_batch_id
      ),
      'downstream', (
        SELECT COALESCE(jsonb_agg(s ORDER BY s.created_at), '[]')
        FROM batch_stage_downstream s WHERE s.batch_id = p_batch_id
      )
    ),

    -- Flask-level data
    'flasks', (
      SELECT COALESCE(jsonb_agg(f ORDER BY f.created_at), '[]')
      FROM batch_flasks f WHERE f.batch_id = p_batch_id
    ),
    'flask_inoculations', (
      SELECT COALESCE(jsonb_agg(r ORDER BY r.created_at), '[]')
      FROM batch_flask_inoculations r WHERE r.batch_id = p_batch_id
    ),
    'flask_endpoints', (
      SELECT COALESCE(jsonb_agg(r ORDER BY r.created_at), '[]')
      FROM batch_flask_endpoints r WHERE r.batch_id = p_batch_id
    ),
    'flask_straining', (
      SELECT COALESCE(jsonb_agg(r ORDER BY r.created_at), '[]')
      FROM batch_flask_straining r WHERE r.batch_id = p_batch_id
    ),
    'flask_extract_addition', (
      SELECT COALESCE(jsonb_agg(r ORDER BY r.created_at), '[]')
      FROM batch_flask_extract_addition r WHERE r.batch_id = p_batch_id
    ),
    'flask_qc_samples', (
      SELECT COALESCE(jsonb_agg(r ORDER BY r.created_at), '[]')
      FROM batch_flask_qc_samples r WHERE r.batch_id = p_batch_id
    ),

    -- Fermentation monitoring
    'fermentation', jsonb_build_object(
      'readings', (
        SELECT COALESCE(jsonb_agg(r ORDER BY r.created_at), '[]')
        FROM batch_fermentation_readings r WHERE r.batch_id = p_batch_id
      ),
      'feeds', (
        SELECT COALESCE(jsonb_agg(r ORDER BY r.created_at), '[]')
        FROM batch_fermentation_feeds r WHERE r.batch_id = p_batch_id
      )
    ),

    -- QC & monitoring
    'ph_readings', (
      SELECT COALESCE(jsonb_agg(r ORDER BY r.created_at), '[]')
      FROM ph_readings r WHERE r.batch_id = p_batch_id
    ),
    'incubation_records', (
      SELECT COALESCE(jsonb_agg(r ORDER BY r.created_at), '[]')
      FROM sample_incubation_records r WHERE r.batch_id = p_batch_id
    ),
    'shelf_life_studies', (
      SELECT COALESCE(jsonb_agg(r ORDER BY r.created_at), '[]')
      FROM shelf_life_studies r WHERE r.batch_id = p_batch_id
    ),

    -- Taste testing
    'taste_panels', (
      SELECT COALESCE(jsonb_agg(t ORDER BY t.created_at), '[]')
      FROM taste_panels t WHERE t.batch_id = p_batch_id
    ),

    -- Issues & deviations
    'deviations', (
      SELECT COALESCE(jsonb_agg(d ORDER BY d.created_at), '[]')
      FROM deviations d WHERE d.batch_id = p_batch_id
    ),

    -- Resources & tasks
    'inventory_usage', (
      SELECT COALESCE(jsonb_agg(u ORDER BY u.created_at), '[]')
      FROM inventory_usage u WHERE u.batch_id = p_batch_id
    ),
    'tasks', (
      SELECT COALESCE(jsonb_agg(t ORDER BY t.created_at), '[]')
      FROM tasks t WHERE t.batch_id = p_batch_id
    ),

    -- Audit trail
    'stage_transitions', (
      SELECT COALESCE(jsonb_agg(t ORDER BY t.created_at), '[]')
      FROM stage_transitions t WHERE t.batch_id = p_batch_id
    ),
    'lab_logs', (
      SELECT COALESCE(jsonb_agg(l ORDER BY l.created_at), '[]')
      FROM lab_logs l WHERE l.batch_id = p_batch_id
    ),
    'lab_notebook', (
      SELECT COALESCE(jsonb_agg(e ORDER BY e.created_at), '[]')
      FROM lab_notebook_entries e WHERE e.batch_id = p_batch_id
    ),
    'activity_log', (
      SELECT COALESCE(jsonb_agg(a ORDER BY a.log_date, a.start_time), '[]')
      FROM activity_log a WHERE a.batch_id = p_batch_id
    )

  ) INTO v_result;

  RETURN v_result;
END;
$$;

GRANT EXECUTE ON FUNCTION get_batch_overview(uuid) TO authenticated;
