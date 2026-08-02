text = open(r'C:\Users\LENOVO\AppData\Local\Temp\odr-inspect\ostrowski-dimensionless-reformulation.md', encoding='utf-8').read()
lines = text.splitlines()

with open(r'C:\Users\LENOVO\AppData\Local\Temp\odr-inspect\remaining_checks.txt', 'w', encoding='utf-8') as f:
    # Find all mentions of red-team critique
    f.write("=== RED-TEAM CRITIQUE MENTIONS ===\n")
    for i, line in enumerate(lines):
        if 'red-team' in line.lower() and ('critique' in line.lower() or 'finding' in line.lower() or 'sharp' in line.lower()):
            start = max(0, i-3)
            end = min(len(lines), i+5)
            f.write(f"\n--- L{i+1} ---\n")
            for j in range(start, end):
                f.write(f"L{j+1}: {lines[j]}\n")
    
    # Look for the specific enumerated overclaim corrections
    f.write("\n=== SPECIFIC CORRECTIONS MENTIONED ===\n")
    for i, line in enumerate(lines):
        if 'correct' in line.lower() and ('p-adic ontology' in line.lower() or 'euclidean' in line.lower() or 'adelic path integral' in line.lower()):
            start = max(0, i-3)
            end = min(len(lines), i+5)
            f.write(f"\n--- L{i+1} ---\n")
            for j in range(start, end):
                f.write(f"L{j+1}: {lines[j]}\n")
    
    # Check section 1.3 Scope and Classification for specifics
    f.write("\n=== SECTION 1.3 SCOPE AND CLASSIFICATION (L63-79+) ===\n")
    for i in range(62, min(120, len(lines))):
        f.write(f"L{i+1}: {lines[i]}\n")
    
    # Check the beginning of the Research Roadmap intro more carefully
    f.write("\n=== RESEARCH ROADMAP INTRO (L674-710) ===\n")
    for i in range(673, min(710, len(lines))):
        f.write(f"L{i+1}: {lines[i]}\n")
    
    # Check for contradictory claims - "physics IS rational" vs. the caveat
    f.write("\n=== CONTRADICTION CHECK: 'Physics Is Rational' vs caveats ===\n")
    # Check L296 vs L298
    for i in [292, 296, 298, 302]:
        if i < len(lines):
            f.write(f"L{i}: {lines[i-1]}\n")
    
    # Check if the paper acknowledges WHERE it was previously overclaiming
    f.write("\n=== ACKNOWLEDGMENT OF AUDIT FINDINGS ===\n")
    for i, line in enumerate(lines):
        lower = line.lower()
        if ('audit' in lower or 'v2.3' in lower or 'v3.0' in lower) and ('red' in lower or 'finding' in lower or 'overclaim' in lower or 'correct' in lower):
            f.write(f"L{i+1}: {line.strip()[:300]}\n")
    
print('done')
