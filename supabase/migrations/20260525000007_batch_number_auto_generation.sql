-- Automated batch number generation.
-- Format: OB-YYYY-MM-NNN (e.g. OB-2026-05-001)
-- Counter resets each month. Numbers are assigned atomically — no duplicates
-- even under concurrent inserts.
-- The BEFORE INSERT trigger auto-fills batch_id so the frontend never needs
-- to supply it. It uses planned_start_date if provided, else today.

-- 1. Counter table
CREATE TABLE IF NOT EXISTS batch_number_sequences (
  year  integer NOT NULL,
  month integer NOT NULL,
  last_seq integer NOT NULL DEFAULT 0,
  PRIMARY KEY (year, month)
);

-- Seed: OB-2026-05-001 already exists in production
INSERT INTO batch_number_sequences (year, month, last_seq)
VALUES (2026, 5, 1)
ON CONFLICT (year, month) DO UPDATE
  SET last_seq = GREATEST(batch_number_sequences.last_seq, EXCLUDED.last_seq);

-- 2. Generation function
CREATE OR REPLACE FUNCTION generate_batch_number(p_date date DEFAULT CURRENT_DATE)
RETURNS text
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = public, pg_temp
AS $$
DECLARE
  v_year  integer := EXTRACT(YEAR  FROM p_date)::integer;
  v_month integer := EXTRACT(MONTH FROM p_date)::integer;
  v_seq   integer;
BEGIN
  INSERT INTO batch_number_sequences (year, month, last_seq)
  VALUES (v_year, v_month, 1)
  ON CONFLICT (year, month)
  DO UPDATE SET last_seq = batch_number_sequences.last_seq + 1
  RETURNING last_seq INTO v_seq;

  RETURN 'OB-'
    || v_year::text
    || '-' || LPAD(v_month::text, 2, '0')
    || '-' || LPAD(v_seq::text,   3, '0');
END;
$$;

GRANT EXECUTE ON FUNCTION generate_batch_number(date) TO authenticated;

-- 3. Trigger: auto-fill batch_id on INSERT
CREATE OR REPLACE FUNCTION batches_set_batch_number()
RETURNS trigger
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = public, pg_temp
AS $$
BEGIN
  IF NEW.batch_id IS NULL OR trim(NEW.batch_id) = '' THEN
    NEW.batch_id := generate_batch_number(
      COALESCE(NEW.planned_start_date, CURRENT_DATE)
    );
  END IF;
  RETURN NEW;
END;
$$;

DROP TRIGGER IF EXISTS trg_batches_batch_number ON batches;
CREATE TRIGGER trg_batches_batch_number
BEFORE INSERT ON batches
FOR EACH ROW EXECUTE FUNCTION batches_set_batch_number();
