text = open(r'C:\Users\LENOVO\AppData\Local\Temp\odr-inspect\ostrowski-dimensionless-reformulation.md', encoding='utf-8').read()
lines = text.splitlines()
with open(r'C:\Users\LENOVO\AppData\Local\Temp\odr-inspect\sections.txt', 'w', encoding='utf-8') as f:
    for i, line in enumerate(lines):
        if line.startswith('##') or line.startswith('# '):
            f.write(f"L{i+1}: {line.strip()[:150]}\n")
print('done')
