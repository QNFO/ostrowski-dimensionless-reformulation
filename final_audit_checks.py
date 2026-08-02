text = open(r'C:\Users\LENOVO\AppData\Local\Temp\odr-inspect\ostrowski-dimensionless-reformulation.md', encoding='utf-8').read()
lines = text.splitlines()

with open(r'C:\Users\LENOVO\AppData\Local\Temp\odr-inspect\final_audit.txt', 'w', encoding='utf-8') as f:
    # 1. Check for prediction claims
    f.write("=== PREDICTION CLAIMS ===\n")
    for i, line in enumerate(lines):
        if 'predict' in line.lower() and ('testable' in line.lower() or 'falsif' in line.lower() or 'experiment' in line.lower()):
            f.write(f"L{i+1}: {line.strip()[:300]}\n")
    
    # 2. Check for "IS" claims about physics/p-adic
    f.write("\n=== 'IS' CLAIMS (potential overclaims) ===\n")
    for i, line in enumerate(lines):
        lower = line.lower()
        if ('physics is' in lower or 'universe is' in lower or 'nature is' in lower or 'reality is' in lower) and 'p-adic' not in lower:
            f.write(f"L{i+1}: {line.strip()[:300]}\n")
    
    # 3. Check Final So What claims
    f.write("\n=== FINAL SO WHAT (L803-825) ===\n")
    for i in range(802, min(825, len(lines))):
        f.write(f"L{i+1}: {lines[i]}\n")
    
    # 4. Check for "v2.0.2" references
    f.write("\n=== v2.0.2 REFERENCES ===\n")
    for i, line in enumerate(lines):
        if 'v2.0.2' in line.lower():
            f.write(f"L{i+1}: {line.strip()[:300]}\n")
    
    # 5. Check for proper DOI format
    f.write("\n=== PLACEHOLDER / INCOMPLETE DOIs ===\n")
    for i, line in enumerate(lines):
        if 'XXXXXXXXXX' in line or 'zenodo.' in line.lower() and 'XXXX' in line:
            f.write(f"L{i+1}: {line.strip()[:200]}\n")
    
    # 6. Check for the "AI" disclosure quality
    f.write("\n=== AI DISCLOSURE CONTEXT ===\n")
    for i, line in enumerate(lines):
        if 'artificial intelligence' in line.lower() or 'AI-assisted' in line or 'DeepChat' in line:
            start = max(0, i-3)
            end = min(len(lines), i+5)
            for j in range(start, end):
                f.write(f"L{j+1}: {lines[j]}\n")
            f.write("---\n")
    
    # 7. Check if the paper acknowledges v2.0.2 overclaims have been corrected
    f.write("\n=== ACKNOWLEDGMENT OF V2.0.2 CORRECTIONS ===\n")
    for i, line in enumerate(lines):
        if ('overclaim' in line.lower() or 'correct' in line.lower()) and ('v2' in line.lower() or 'prior' in line.lower() or 'previous' in line.lower()):
            start = max(0, i-2)
            end = min(len(lines), i+3)
            f.write(f"\n--- L{i+1} ---\n")
            for j in range(start, end):
                f.write(f"L{j+1}: {lines[j]}\n")
    
    # 8. Check for claims of "derivation" vs "reframing"
    f.write("\n=== 'DERIVATION' LANGUAGE ===\n")
    for i, line in enumerate(lines):
        if 'deriv' in line.lower() and ('first principle' in line.lower() or 'from scratch' in line.lower()):
            f.write(f"L{i+1}: {line.strip()[:300]}\n")
    
    # 9. Check for numerology red flags
    f.write("\n=== NUMEROLOGY CHECKS ===\n")
    for i, line in enumerate(lines):
        if 'coincidence' in line.lower() or 'remarkable' in line.lower() and 'numer' in line.lower():
            f.write(f"L{i+1}: {line.strip()[:300]}\n")
    
    # 10. "Physics Is Rational" section full text
    f.write("\n=== PHYSICS IS RATIONAL (L288-315) ===\n")
    for i in range(287, min(315, len(lines))):
        f.write(f"L{i+1}: {lines[i]}\n")
    
print('done')
