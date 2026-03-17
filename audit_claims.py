import os
import re

def search_directory_for_terms(directory, terms):
    results = {term: [] for term in terms}
    
    for root, _, files in os.walk(directory):
        if "_archive_scripts" in root or ".vercel" in root or ".git" in root:
            continue
            
        for file in files:
            if file.endswith(".html"):
                filepath = os.path.join(root, file)
                
                with open(filepath, 'r', encoding='utf-8') as f:
                    try:
                        lines = f.readlines()
                        for i, line in enumerate(lines):
                            for term in terms:
                                # Simple case-insensitive search
                                if re.search(r'\b' + term + r'\b', line, re.IGNORECASE):
                                    results[term].append(f"{file} (Line {i+1}): {line.strip()[:100]}...")
                    except Exception as e:
                        print(f"Error reading {filepath}: {e}")
                        
    return results

directory_to_scan = "e:/OXYBIO"

# Drug/Medical Restricted Terms for Food Products
restricted_medical_terms = [
    "cure", "treat", "diagnose", "prevent", "disease", "clinical", 
    "pharmacological", "pharma", "drug", "medicine", "medical", 
    "pill", "therapy", "therapeutic", "dosage", "dose", "prescription"
]

# Exaggerated/Marketing/False Claim terms
exaggerated_terms = [
    "guarantee", "perfect", "ultimate", "instant", "miracle", 
    "breakthrough", "magic", "100% absorption", "secret"
]

print("--- RESTRICTED MEDICAL TERMS FOUND ---")
medical_results = search_directory_for_terms(directory_to_scan, restricted_medical_terms)
for term, hits in medical_results.items():
    if hits:
        print(f"\n[!] Term '{term}' found {len(hits)} times:")
        for hit in hits[:5]: # Print max 5 to keep output sane
            print(f"  - {hit}")

print("\n--- EXAGGERATED CLAIMS FOUND ---")
exaggerated_results = search_directory_for_terms(directory_to_scan, exaggerated_terms)
for term, hits in exaggerated_results.items():
    if hits:
        print(f"\n[!] Term '{term}' found {len(hits)} times:")
        for hit in hits[:5]:
            print(f"  - {hit}")
