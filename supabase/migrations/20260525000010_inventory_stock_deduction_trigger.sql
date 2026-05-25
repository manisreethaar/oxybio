-- Auto-deduct from inventory_stock.current_quantity when a batch logs usage.
-- Adds stock_id FK to inventory_usage so we know which specific lot was consumed.

ALTER TABLE inventory_usage
  ADD COLUMN IF NOT EXISTS stock_id uuid REFERENCES inventory_stock(id) ON DELETE SET NULL;

CREATE INDEX IF NOT EXISTS idx_inventory_usage_stock_id ON inventory_usage(stock_id);

CREATE OR REPLACE FUNCTION inventory_usage_deduct_stock()
RETURNS trigger
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = public, pg_temp
AS $$
DECLARE
  v_current numeric;
BEGIN
  IF NEW.stock_id IS NULL THEN
    RETURN NEW;
  END IF;

  SELECT current_quantity INTO v_current
  FROM inventory_stock WHERE id = NEW.stock_id FOR UPDATE;

  IF v_current < NEW.quantity_used THEN
    RAISE EXCEPTION 'Insufficient stock: available %, requested %', v_current, NEW.quantity_used;
  END IF;

  UPDATE inventory_stock
  SET current_quantity = current_quantity - NEW.quantity_used,
      status = CASE
        WHEN (current_quantity - NEW.quantity_used) <= 0 THEN 'Depleted'
        ELSE status
      END
  WHERE id = NEW.stock_id;

  INSERT INTO inventory_movements (stock_id, type, quantity, purpose, notes, issued_by)
  VALUES (
    NEW.stock_id, 'consumption', NEW.quantity_used,
    'Batch usage',
    'Batch ID: ' || coalesce(NEW.batch_id::text, 'N/A'),
    NEW.logged_by
  );

  RETURN NEW;
END;
$$;

DROP TRIGGER IF EXISTS trg_inventory_usage_deduct ON inventory_usage;
CREATE TRIGGER trg_inventory_usage_deduct
AFTER INSERT ON inventory_usage
FOR EACH ROW EXECUTE FUNCTION inventory_usage_deduct_stock();
