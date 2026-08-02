import re

path = r'C:\Users\LENOVO\AppData\Local\Temp\odr-inspect\ostrowski-dimensionless-reformulation.md'
with open(path, 'r', encoding='utf-8') as f:
    md = f.read()

# Fix the DOI and version in YAML (was 21755603/v4.0 from the downloaded v4.0.1 source)
md = md.replace('doi: "10.5281/zenodo.21755603"', 'doi: "10.5281/zenodo.21755771"')
md = md.replace('version: "4.0"', 'version: "4.0.2"')
# Fix title to v4.0.2
md = md.replace('v4.0: A Place-Democratic', 'v4.0.2: A Place-Democratic')
md = md.replace('Reformulation v4.0:', 'Reformulation v4.0.2:')

# Sanitize control chars + emoji (same as pipeline)
out = []
for ch in md:
    cp = ord(ch)
    if cp < 32 and cp not in (10, 13, 9):
        continue
    if 0x1F000 <= cp <= 0x1FAFF or 0x2600 <= cp <= 0x26FF or 0x2B00 <= cp <= 0x2BFF:
        continue
    out.append(ch)
md = ''.join(out)
md = md.replace('\u274c', '\u2717')
md = md.replace('\u2705', '\u2713')

with open(path, 'w', encoding='utf-8') as f:
    f.write(md)

print('DOI/version fixed, control chars + emoji sanitized')
print('Size:', len(md))
print('tabs:', md.count(chr(9)))
