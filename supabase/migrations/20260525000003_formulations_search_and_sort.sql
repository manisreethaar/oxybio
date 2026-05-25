-- Full-text search vector, indexes for filtering/sorting, and a latest-version view.

-- 1. tsvector column for full-text search
ALTER TABLE formulations ADD COLUMN IF NOT EXISTS search_vector tsvector;

-- 2. Trigger function to keep search_vector current
CREATE OR REPLACE FUNCTION formulations_build_search_vector()
RETURNS trigger
LANGUAGE plpgsql AS $$
BEGIN
  NEW.search_vector :=
    setweight(to_tsvector('simple', coalesce(NEW.code, '')), 'A') ||
    setweight(to_tsvector('simple', coalesce(NEW.name, '')), 'A') ||
    setweight(to_tsvector('simple', coalesce(NEW.ingredients, '')), 'B') ||
    setweight(to_tsvector('simple', coalesce(NEW.notes, '')), 'C');
  RETURN NEW;
END;
$$;

DROP TRIGGER IF EXISTS trg_formulations_search_vector ON formulations;
CREATE TRIGGER trg_formulations_search_vector
BEFORE INSERT OR UPDATE OF code, name, ingredients, notes
ON formulations
FOR EACH ROW EXECUTE FUNCTION formulations_build_search_vector();

-- 3. Back-fill existing rows
UPDATE formulations SET search_vector =
  setweight(to_tsvector('simple', coalesce(code, '')), 'A') ||
  setweight(to_tsvector('simple', coalesce(name, '')), 'A') ||
  setweight(to_tsvector('simple', coalesce(ingredients, '')), 'B') ||
  setweight(to_tsvector('simple', coalesce(notes, '')), 'C');

-- 4. Indexes
CREATE INDEX IF NOT EXISTS idx_formulations_search       ON formulations USING GIN(search_vector);
CREATE INDEX IF NOT EXISTS idx_formulations_status       ON formulations(status);
CREATE INDEX IF NOT EXISTS idx_formulations_code         ON formulations(code);
CREATE INDEX IF NOT EXISTS idx_formulations_created_at   ON formulations(created_at DESC);
CREATE INDEX IF NOT EXISTS idx_formulations_code_version ON formulations(code, version DESC);
CREATE INDEX IF NOT EXISTS idx_formulations_base_version ON formulations(base_version_id) WHERE base_version_id IS NOT NULL;

-- 5. View: one row per recipe code, always the latest version
CREATE OR REPLACE VIEW formulations_latest AS
SELECT DISTINCT ON (code) *
FROM formulations
ORDER BY code, version DESC, created_at DESC;
