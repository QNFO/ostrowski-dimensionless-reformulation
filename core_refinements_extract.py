text = open(r'C:\Users\LENOVO\AppData\Local\Temp\odr-inspect\ostrowski-dimensionless-reformulation.md', encoding='utf-8').read()
lines = text.splitlines()

with open(r'C:\Users\LENOVO\AppData\Local\Temp\odr-inspect\core_refinements.txt', 'w', encoding='utf-8') as f:
    # Find lines containing "refinement" or "core" or around line 25 and following 500 lines
    for i, line in enumerate(lines):
        if 'refinement' in line.lower() or 'core' in line.lower() or 'overclaim' in line.lower() or 'correct' in line.lower():
            f.write(f"L{i+1}: {line.strip()[:250]}\n")
    
    # Also extract lines 1-200 for full context of refinements
    f.write("\n\n=== LINES 1-200 (full) ===\n")
    for i in range(min(200, len(lines))):
        f.write(f"L{i+1}: {lines[i]}\n")
print('done')
