-- Fix: batches_status_check was missing 'scheduled' and 'in-progress',
-- causing batch creation from the scheduling form to fail.
ALTER TABLE batches DROP CONSTRAINT batches_status_check;

ALTER TABLE batches ADD CONSTRAINT batches_status_check
  CHECK (status = ANY (ARRAY[
    'scheduled',    -- batch created, not yet started
    'planned',      -- kept for backwards compat
    'in-progress',  -- batch actively running
    'fermenting',   -- fermentation stage
    'qc-hold',      -- awaiting QC clearance
    'released',     -- passed QC, released
    'rejected',     -- failed QC
    'deviation'     -- batch had a deviation
  ]));
