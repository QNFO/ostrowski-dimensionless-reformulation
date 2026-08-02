import re

text = open(r'C:\Users\LENOVO\AppData\Local\Temp\odr-inspect\ostrowski-dimensionless-reformulation.md', encoding='utf-8').read()
lines = text.splitlines()

with open(r'C:\Users\LENOVO\AppData\Local\Temp\odr-inspect\reputation_audit.txt', 'w', encoding='utf-8') as f:
    # 1. Overclaim patterns
    patterns = [
        ('overclaim', r'overclaim'),
        ('p-adic ontology', r'p-adic'),
        ('definitive', r'definitive'),
        ('manifesto', r'manifesto'),
        ('derived from first', r'first principle'),
        ('discover', r'\bdiscover'),
        ('numerolog', r'numerolog'),
        ('v2.0.2', r'v2\.0\.2'),
        ('v2.0', r'v2\.0'),
        ('red-team', r'red.team'),
        ('CALIBRATION-CAP', r'CALIBRATION'),
        ('speculative', r'\[speculative\]'),
        ('established', r'\[established\]'),
        ('uncertain', r'\[uncertain\]'),
        ('honesty', r'honest'),
        ('claim', r'\bclaim'),
        ('ontology', r'ontology'),
        ('physics IS', r'physics.*\bIS\b'),
        ('CAN BE', r'CAN BE'),
        ('sigma', r'sigma'),
        ('p-value', r'p.value'),
        ('post-hoc', r'post.hoc'),
    ]
    
    f.write("=== REPUTATION AUDIT: KEYWORD ANALYSIS ===\n\n")
    for label, pattern in patterns:
        matches = []
        for i, line in enumerate(lines):
            if re.search(pattern, line, re.IGNORECASE):
                matches.append((i+1, line.strip()[:200]))
        if matches:
            f.write(f"\n--- {label} ({len(matches)} matches) ---\n")
            for ln, txt in matches[:15]:
                f.write(f"  L{ln}: {txt}\n")
    
    # 2. Check for AI-generated filler patterns
    f.write("\n\n=== AI FILLER PATTERN CHECK ===\n")
    filler_patterns = [
        'delve into', 'in conclusion', 'it is worth noting', 'furthermore',
        'moreover', 'additionally', 'in summary', 'as previously mentioned',
        'it should be noted', 'it is important to note', 'from this we can see',
        'to this end', 'in this regard', 'in other words',
    ]
    for pat in filler_patterns:
        count = 0
        for i, line in enumerate(lines):
            if pat.lower() in line.lower():
                count += 1
        if count > 3:
            f.write(f"  WARNING: '{pat}' appears {count} times (potential AI filler)\n")
    
    # 3. Check for certainty labeling throughout the paper
    f.write("\n\n=== CERTAINTY LABEL ANALYSIS ===\n")
    spec_count = sum(1 for line in lines if '[speculative]' in line.lower())
    est_count = sum(1 for line in lines if '[established' in line.lower())
    uncer_count = sum(1 for line in lines if '[uncertain' in line.lower())
    calib_count = sum(1 for line in lines if 'calibration' in line.lower())
    f.write(f"  [speculative] count: {spec_count}\n")
    f.write(f"  [established] count: {est_count}\n")
    f.write(f"  [uncertain] count: {uncer_count}\n")
    f.write(f"  calibration-related: {calib_count}\n")
    
    # 4. Check for false-precision numbers
    f.write("\n\n=== NUMERICAL PRECISION CHECK ===\n")
    # Find numbers with many significant digits
    for i, line in enumerate(lines):
        # Match numbers like 1.054571817, 6.67430, etc.
        matches = re.findall(r'\b\d+\.\d{8,}\b', line)
        if matches:
            f.write(f"  L{i+1}: High-precision numbers: {matches}\n")
    
    # 5. Check for percentage/sigma claims
    f.write("\n\n=== SIGMA/PERCENTAGE CLAIMS ===\n")
    for i, line in enumerate(lines):
        if re.search(r'\d+\s*σ', line) or re.search(r'\d+\s*sigma', line, re.IGNORECASE):
            f.write(f"  L{i+1}: Sigma claim: {line.strip()[:200]}\n")
        if re.search(r'\d+\.?\d*\s*%', line) and not re.search(r'c\s*=', line):
            f.write(f"  L{i+1}: Percentage: {line.strip()[:200]}\n")
    
    f.write("\n\n=== AUDIT COMPLETE ===\n")
print('done')
