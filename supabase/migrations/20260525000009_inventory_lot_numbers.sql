-- Auto-generate internal lot numbers (LOT-YYYY-MM-NNN) when stock is received
-- without a supplier lot number, replacing the "UN-LOT" fallback in the UI.

CREATE TABLE IF NOT EXISTS lot_number_sequences (
  year     integer NOT NULL,
  month    integer NOT NULL,
  last_seq integer NOT NULL DEFAULT 0,
  PRIMARY KEY (year, month)
);

CREATE OR REPLACE FUNCTION generate_lot_number(p_date date DEFAULT CURRENT_DATE)
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
  INSERT INTO lot_number_sequences (year, month, last_seq)
  VALUES (v_year, v_month, 1)
  ON CONFLICT (year, month)
  DO UPDATE SET last_seq = lot_number_sequences.last_seq + 1
  RETURNING last_seq INTO v_seq;

  RETURN 'LOT-'
    || v_year::text
    || '-' || LPAD(v_month::text, 2, '0')
    || '-' || LPAD(v_seq::text,   3, '0');
END;
$$;

GRANT EXECUTE ON FUNCTION generate_lot_number(date) TO authenticated;

CREATE OR REPLACE FUNCTION inventory_stock_set_lot_number()
RETURNS trigger
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = public, pg_temp
AS $$
BEGIN
  IF NEW.supplier_batch_number IS NULL OR trim(NEW.supplier_batch_number) = '' THEN
    NEW.supplier_batch_number := generate_lot_number(CURRENT_DATE);
  END IF;
  RETURN NEW;
END;
$$;

DROP TRIGGER IF EXISTS trg_inventory_stock_lot_number ON inventory_stock;
CREATE TRIGGER trg_inventory_stock_lot_number
BEFORE INSERT ON inventory_stock
FOR EACH ROW EXECUTE FUNCTION inventory_stock_set_lot_number();

-- Back-fill existing blank lot numbers
UPDATE inventory_stock
SET supplier_batch_number = generate_lot_number(created_at::date)
WHERE supplier_batch_number IS NULL OR trim(supplier_batch_number) = '';
