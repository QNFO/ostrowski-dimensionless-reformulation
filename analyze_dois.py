import re
with open(r'C:\Users\LENOVO\AppData\Local\Temp\odr-inspect\ostrowski-dimensionless-reformulation.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

with open(r'C:\Users\LENOVO\AppData\Local\Temp\odr-inspect\doi_analysis.txt', 'w', encoding='utf-8') as out:
    out.write('=== ALL DOI LINES WITH CONTEXT ===\n')
    for i, line in enumerate(lines, 1):
        if '10.5281/zenodo' in line:
            clean = line.rstrip()[:250]
            out.write(f'L{i}: {clean}\n')
        
    out.write('\n=== Inline DOIs vs Reference DOIs ===\n')
    inline_dois = set()
    ref_dois = set()
    in_refs = False
    for i, line in enumerate(lines):
        if line.strip().startswith('## References'):
            in_refs = True
            continue
        if in_refs and line.strip().startswith('##'):
            in_refs = False
        dois = re.findall(r'10\.5281/zenodo\.\d+', line)
        for d in dois:
            if in_refs:
                ref_dois.add(d)
            elif i < 10 and 'doi:' in line.lower():
                pass
            else:
                inline_dois.add(d)

    out.write('Inline DOIs (body):\n')
    for d in sorted(inline_dois):
        out.write(f'  {d}\n')
    out.write(f'  (total: {len(inline_dois)})\n')
    out.write('\nReference-section DOIs:\n')
    for d in sorted(ref_dois):
        out.write(f'  {d}\n')
    out.write(f'  (total: {len(ref_dois)})\n')
    out.write('\nIn body but NOT in references:\n')
    only_body = sorted(inline_dois - ref_dois)
    for d in only_body:
        out.write(f'  {d}\n')
    out.write(f'  (total: {len(only_body)})\n')
    out.write('\nIn references but NOT in body:\n')
    only_ref = sorted(ref_dois - inline_dois)
    for d in only_ref:
        out.write(f'  {d}\n')
    out.write(f'  (total: {len(only_ref)})\n')
    
    # DOI collision detection
    out.write('\n=== DOI COLLISION DETECTION ===\n')
    doi_to_paper = {}
    for i, line in enumerate(lines, 1):
        if '10.5281/zenodo.' in line:
            dois = re.findall(r'10\.5281/zenodo\.\d+', line)
            for d in dois:
                # Try to extract paper title/context
                context = line.strip()[:150]
                if d not in doi_to_paper:
                    doi_to_paper[d] = []
                doi_to_paper[d].append(f'L{i}: {context}')
    
    for d, contexts in doi_to_paper.items():
        if len(contexts) > 1:
            # Check if same paper name
            names = set()
            for c in contexts:
                names.add(c[:80])
            if len(names) > 1:
                out.write(f'\nDOI {d} appears in multiple contexts:\n')
                for c in contexts:
                    out.write(f'  {c}\n')
    
    # Check for truncated DOI
    out.write('\n=== TRUNCATED/INCOMPLETE DOI ===\n')
    for i, line in enumerate(lines, 1):
        if '10.5281/zenodo)' in line or '10.5281/zenodo ' in line:
            if '10.5281/zenodo.' not in line:
                out.write(f'L{i}: {line.strip()[:200]}\n')
        if '10.5281/zenodo)' in line:
            out.write(f'L{i} (truncated): {line.strip()[:200]}\n')
    
    out.write('\n=== GITHUB URLs ===\n')
    for i, line in enumerate(lines, 1):
        if 'github.com' in line.lower():
            out.write(f'L{i}: {line.strip()[:200]}\n')
    
    out.write('\n=== VERSION REFERENCES ===\n')
    for i, line in enumerate(lines, 1):
        if re.search(r'v\d+\.\d+', line) and '10.5281' not in line and 'version' not in line.lower():
            pass  # too many false positives
        if 'v2.0.2' in line or 'v2.1' in line or 'v3.0' in line or 'v4.0' in line:
            if '10.5281' in line:
                out.write(f'L{i}: {line.strip()[:200]}\n')
    
    # Papers cited inline but not in references
    out.write('\n=== PAPERS CITED INLINE (WITH DOIs) BUT MISSING FROM REFERENCE LIST ===\n')
    inline_papers = []  # DOI -> paper name
    for i, line in enumerate(lines, 1):
        if i > 10 and '10.5281/zenodo.' in line and 'DOI:' in line:
            match = re.search(r'\*\*([^*]+?)\*\*\s*\(?DOI:\s*(10\.5281/zenodo\.\d+)', line)
            if match:
                name = match.group(1).strip()
                doi = match.group(2)
                inline_papers.append((doi, name, i))
    
    for doi, name, ln in inline_papers:
        out.write(f'  [{doi}] L{ln}: {name}\n')
    
    # Count total unique DOIs
    all_dois = inline_dois | ref_dois
    out.write(f'\nTotal unique DOIs: {len(all_dois)}\n')
    
    # Placeholder check
    out.write('\n=== PLACEHOLDER CHECK ===\n')
    for i, line in enumerate(lines, 1):
        if 'XXXXXXXXXX' in line:
            out.write(f'L{i}: {line.strip()[:200]}\n')

print('Analysis complete, saved to doi_analysis.txt')
