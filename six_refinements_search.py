text = open(r'C:\Users\LENOVO\AppData\Local\Temp\odr-inspect\ostrowski-dimensionless-reformulation.md', encoding='utf-8').read()
lines = text.splitlines()

with open(r'C:\Users\LENOVO\AppData\Local\Temp\odr-inspect\six_refinements.txt', 'w', encoding='utf-8') as f:
    # Look for "six" near "refinement" or "refinements" or numbered refinements
    for i, line in enumerate(lines):
        lower = line.lower()
        if 'six' in lower and ('refine' in lower or 'overclaim' in lower or 'correct' in lower):
            # Print surrounding context
            start = max(0, i-3)
            end = min(len(lines), i+5)
            f.write(f"\n--- Match at L{i+1} ---\n")
            for j in range(start, end):
                f.write(f"L{j+1}: {lines[j]}\n")
    
    # Also look for bullet points with "Refinement" or numbered refinements
    f.write("\n\n=== BULLET POINTS WITH 'REFINEMENT' ===\n")
    for i, line in enumerate(lines):
        if ('refinement' in line.lower() or 'refinements' in line.lower()) and ('-' == line.strip()[:1] or '**Refine' in line or '1.' == line.strip()[:2] or '### Re' in line):
            f.write(f"L{i+1}: {line.strip()[:250]}\n")

    # Also look for lines about corrected overclaims
    f.write("\n\n=== CORRECTED OVERCLAIM CONTEXT ===\n")
    for i, line in enumerate(lines):
        if 'overclaim' in line.lower() and 'p-adic' in line.lower():
            start = max(0, i-5)
            end = min(len(lines), i+10)
            f.write(f"\n--- Match at L{i+1} ---\n")
            for j in range(start, end):
                f.write(f"L{j+1}: {lines[j]}\n")
    
    # Also: search for "refined" or "refinement" in the paper body after the abstract
    f.write("\n\n=== ALL 'REFINEMENT' / 'REFINED' LINES ===\n")
    for i, line in enumerate(lines):
        if 'refine' in line.lower():
            f.write(f"L{i+1}: {line.strip()[:250]}\n")
print('done')
