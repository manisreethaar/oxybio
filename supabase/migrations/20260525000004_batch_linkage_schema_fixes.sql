-- Fix batch linkage across modules:
-- 1. activity_log.batch_id was TEXT — convert to UUID and add FK
-- 2. taste_panels had no batch_id at all — add with FK
-- 3. deviations had no batch_id — add with FK so issues are traceable to a batch

ALTER TABLE activity_log
  ALTER COLUMN batch_id TYPE uuid USING batch_id::uuid;

ALTER TABLE activity_log
  ADD CONSTRAINT activity_log_batch_id_fkey
  FOREIGN KEY (batch_id) REFERENCES batches(id) ON DELETE SET NULL;

ALTER TABLE taste_panels
  ADD COLUMN IF NOT EXISTS batch_id uuid REFERENCES batches(id) ON DELETE SET NULL;

CREATE INDEX IF NOT EXISTS idx_taste_panels_batch_id ON taste_panels(batch_id);

ALTER TABLE deviations
  ADD COLUMN IF NOT EXISTS batch_id uuid REFERENCES batches(id) ON DELETE SET NULL;

CREATE INDEX IF NOT EXISTS idx_deviations_batch_id ON deviations(batch_id);
