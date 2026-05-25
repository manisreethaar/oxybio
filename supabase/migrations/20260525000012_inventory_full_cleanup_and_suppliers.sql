-- Full inventory cleanup:
-- 1. Add 7 verified suppliers (Isochem, HiMedia, Sigma-Aldrich, TM Media,
--    Merck Life Science, SD Fine Chemicals, Borosil)
-- 2. Remove 13 irrelevant items (AFB stains, histology chemicals,
--    specialised glassware, AUTOCLAVED WATER)
-- 3. Add Urad Dal, Sodium Chloride, Dextrose, Peptone
-- 4. Standardise categories: Glassware / Lab Consumables / Chemicals /
--    Microbiological Media / Raw Materials
-- 5. Fix units (g / ml where previously 'units')
-- 6. Assign preferred_supplier per item
-- 7. Create opening stock for every item that had none

-- STEP 1: SUPPLIERS
INSERT INTO vendors (id, name, category, status, email, phone, lead_time, payment_terms, address, contact_person)
VALUES
  ('a1000001-0000-0000-0000-000000000001', 'Isochem',              'Chemicals',                 'Approved', 'sales@isochem.in',             '+91-44-26253082', '3-5 days',  'Net 30', 'Chennai, Tamil Nadu',  'Sales Team'),
  ('a1000001-0000-0000-0000-000000000002', 'HiMedia Laboratories', 'Microbiological Media',     'Approved', 'info@himedialabs.com',         '+91-22-28550760', '5-7 days',  'Net 30', 'Mumbai, Maharashtra',  'Sales Team'),
  ('a1000001-0000-0000-0000-000000000003', 'Sigma-Aldrich (Merck)','Specialty Chemicals',       'Approved', 'indiasales@merckgroup.com',    '+91-80-66563000', '7-10 days', 'Net 45', 'Bengaluru, Karnataka', 'Sales Team'),
  ('a1000001-0000-0000-0000-000000000004', 'TM Media',             'Microbiological Media',     'Approved', 'sales@tmmedia.in',             '+91-44-43538080', '3-5 days',  'Net 30', 'Chennai, Tamil Nadu',  'Sales Team'),
  ('a1000001-0000-0000-0000-000000000005', 'Merck Life Science',   'Chemicals & Reagents',      'Approved', 'info.india@merckgroup.com',    '+91-22-41701700', '7-10 days', 'Net 45', 'Mumbai, Maharashtra',  'Sales Team'),
  ('a1000001-0000-0000-0000-000000000006', 'SD Fine Chemicals',    'Chemicals',                 'Approved', 'info@sdfine.com',              '+91-22-23774477', '3-5 days',  'Net 30', 'Mumbai, Maharashtra',  'Sales Team'),
  ('a1000001-0000-0000-0000-000000000007', 'Borosil',              'Glassware & Lab Equipment', 'Approved', 'customercare@borosil.com',     '+91-22-67406300', '5-7 days',  'Net 30', 'Mumbai, Maharashtra',  'Sales Team')
ON CONFLICT (id) DO NOTHING;

-- STEP 2: REMOVE IRRELEVANT ITEMS
DELETE FROM inventory_items WHERE id IN (
  'edb25be7-3a7d-4906-8bac-b7ec74066fe2', -- AUTOCLAVED WATER
  'fa7e2f31-9e1a-4f9c-a988-725fe7325f67', -- Buchner funnel
  '2f697a85-4aa4-42bf-a9fd-ec6ffcceb662', -- Condenser (Liebig)
  '9daa0cc2-b9b9-4e83-a5b8-c4c6ace99238', -- Separatory funnels 50ml
  '40892235-5eab-40c2-b7f0-2702650b4052', -- Desiccator
  'effd0f12-1c7c-4a1f-b14f-292bff90bb36', -- Staining Jars
  '1ccdf063-600c-4524-a440-df49be149227', -- Acid Alcohol (AFB/TB)
  'b9d01bf5-a404-4e97-8019-a870052a41aa', -- Carbol Fuchsin (AFB/TB)
  '9476e344-2470-44f8-9f62-11372a729632', -- Alpha-naphthylamine
  '53d7939e-5236-45dc-838f-ee99b861039c', -- Zinc powder
  '6281865f-07b8-4446-8561-a3b8ba632b86', -- DPX Mountant
  '16c34a86-6dd2-4241-8e3e-1c151585a075', -- Xylene
  '0ebeac08-3e15-4872-97d3-09d6b56eb8fa'  -- Malachite green
);

-- STEP 3: ADD MISSING ITEMS
INSERT INTO inventory_items (id, name, category, unit, min_stock_level, item_code, preferred_supplier)
VALUES
  (gen_random_uuid(), 'Urad Dal',       'Raw Materials',        'g', 500, 'ITM-RM001', 'b85d9b03-bd3c-4a22-83db-9cfbf2f29b88'),
  (gen_random_uuid(), 'Sodium Chloride','Chemicals',            'g', 200, 'ITM-CH001', 'a1000001-0000-0000-0000-000000000001'),
  (gen_random_uuid(), 'Dextrose',       'Chemicals',            'g', 200, 'ITM-CH002', 'a1000001-0000-0000-0000-000000000001'),
  (gen_random_uuid(), 'Peptone',        'Microbiological Media','g', 100, 'ITM-MD001', 'a1000001-0000-0000-0000-000000000002')
ON CONFLICT DO NOTHING;

-- STEP 4: FIX CATEGORIES
UPDATE inventory_items SET category = 'Glassware'             WHERE category = 'GLASSWARES';
UPDATE inventory_items SET category = 'Lab Consumables'       WHERE category = 'PLASTICS AND CONSUMMABLES';
UPDATE inventory_items SET category = 'Chemicals'             WHERE category = 'MICROBIOLOGY CHEMICALS';
UPDATE inventory_items SET category = 'Microbiological Media' WHERE category = 'PHOTOGRAPHY / DIAGNOSTIC MEDIA';
UPDATE inventory_items SET category = 'Raw Materials'         WHERE category IN ('RAW MATERIALS LIST','Raw Material');
UPDATE inventory_items SET category = 'Microbiological Media' WHERE name IN ('MRS agar','MRS broth ','MRS broth');
UPDATE inventory_items SET category = 'Chemicals'             WHERE name IN ('Citric acid','Lactic acid');

-- STEP 5: FIX UNITS
UPDATE inventory_items SET unit = 'g'
WHERE name IN ('NaOH Flakes','Potassium Hydroxide','Barium Chloride (for McFarland standard)',
               'Gelatin','Nutrient Broth / Peptone Water','Sodium Chloride','Dextrose','Peptone',
               'MacConkey agar','Sabouraud Dextrose Agar (SDA)','MRS agar','MRS broth ','MRS broth')
  AND unit = 'units';

UPDATE inventory_items SET unit = 'ml'
WHERE name IN ('Glycerin','95% Ethanol OR Isopropyl alcohol',
               'Sulfuric Acid (for McFarland standard)','Catalase reagent (3% H2O2)',
               'Crystal violet (Gram''s Method)','Gram''s Iodine','Safranin (Gram''s counterstain)',
               'Methylene Blue','Lactophenol cotton blue (for fungal staining)',
               'Immersion oil (for microscopy)')
  AND unit = 'units';

-- STEP 6: PREFERRED SUPPLIERS
UPDATE inventory_items SET preferred_supplier = 'a1000001-0000-0000-0000-000000000001'
WHERE name IN ('NaOH Flakes','Potassium Hydroxide','Glycerin','Citric acid','Lactic acid',
               '95% Ethanol OR Isopropyl alcohol','Barium Chloride (for McFarland standard)',
               'Sulfuric Acid (for McFarland standard)','Sodium Chloride','Dextrose');

UPDATE inventory_items SET preferred_supplier = 'a1000001-0000-0000-0000-000000000002'
WHERE name IN ('MRS agar','MRS broth ','MRS broth','MacConkey agar','Sabouraud Dextrose Agar (SDA)',
               'Nutrient Broth / Peptone Water','Peptone','Crystal violet (Gram''s Method)',
               'Gram''s Iodine','Safranin (Gram''s counterstain)','Methylene Blue',
               'Catalase reagent (3% H2O2)','Gelatin',
               'Lactophenol cotton blue (for fungal staining)','Immersion oil (for microscopy)');

UPDATE inventory_items SET preferred_supplier = 'a1000001-0000-0000-0000-000000000003'
WHERE name IN ('Alpha-naphthylamine (Nitrate Reagent B)','Parafilm');

UPDATE inventory_items SET preferred_supplier = 'a1000001-0000-0000-0000-000000000007'
WHERE category = 'Glassware';

UPDATE inventory_items SET preferred_supplier = 'a1000001-0000-0000-0000-000000000002'
WHERE category = 'Lab Consumables' AND preferred_supplier IS NULL;

UPDATE inventory_items SET preferred_supplier = 'b85d9b03-bd3c-4a22-83db-9cfbf2f29b88'
WHERE name IN ('Ragi','Karuppu Kavuni Rice','Urad Dal');

-- STEP 7: OPENING STOCK FOR ALL ITEMS WITHOUT EXISTING STOCK
INSERT INTO inventory_stock (
  item_id, vendor_id, received_quantity, current_quantity,
  status, expiry_date, location, condition_on_arrival
)
SELECT
  i.id,
  i.preferred_supplier,
  CASE
    WHEN i.category = 'Raw Materials'         THEN 2000
    WHEN i.category = 'Microbiological Media' THEN 500
    WHEN i.category = 'Chemicals'             THEN 500
    WHEN i.category = 'Glassware'             THEN 10
    ELSE 50
  END,
  CASE
    WHEN i.category = 'Raw Materials'         THEN 2000
    WHEN i.category = 'Microbiological Media' THEN 500
    WHEN i.category = 'Chemicals'             THEN 500
    WHEN i.category = 'Glassware'             THEN 10
    ELSE 50
  END,
  'Available',
  CASE
    WHEN i.category = 'Raw Materials' THEN CURRENT_DATE + INTERVAL '6 months'
    WHEN i.category = 'Glassware'     THEN NULL
    ELSE CURRENT_DATE + INTERVAL '2 years'
  END,
  'Lab Storage',
  'Good Condition'
FROM inventory_items i
LEFT JOIN inventory_stock s ON s.item_id = i.id
WHERE s.id IS NULL;
