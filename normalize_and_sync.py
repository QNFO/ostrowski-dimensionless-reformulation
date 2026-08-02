import re, sys, io, os, json, urllib.request

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

# ============ STEP A: Normalize tables in the ODR source markdown ============
DIR = r'C:\Users\LENOVO\AppData\Local\Temp\odr-inspect'
MD = os.path.join(DIR, 'ostrowski-dimensionless-reformulation.md')

def normalize_tables(md_text):
    lines = md_text.split('\n')
    out = []
    i = 0
    fixed = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        if stripped.startswith('|') and '|' in stripped[1:-1]:
            block = []
            j = i
            while j < len(lines):
                s = lines[j].strip()
                if s.startswith('|'):
                    block.append(lines[j])
                    j += 1
                elif s == '' and j + 1 < len(lines) and lines[j + 1].strip().startswith('|'):
                    j += 1
                else:
                    break
            if len(block) >= 2:
                out.extend(block)
                fixed += 1
                i = j
                continue
        out.append(line)
        i += 1
    return '\n'.join(out), fixed

md = open(MD, encoding='utf-8').read()
norm, n = normalize_tables(md)
print(f'Source: {len(md)} -> {len(norm)} chars, {n} tables normalized')

if norm != md:
    open(MD, 'w', encoding='utf-8').write(norm)
    print('Wrote normalized source back')

# ============ STEP B: Update D1 body_md with normalized content ============
TOKEN_CF = os.environ.get('CLOUDFLARE_API_TOKEN')
if TOKEN_CF:
    ACCOUNT = 'edb167b78c9fb901ea5bca3ce58ccc4b'
    DB = '70a58cb3-b2cd-498d-877f-ecca86859a22'
    URL = f'https://api.cloudflare.com/client/v4/accounts/{ACCOUNT}/d1/database/{DB}/query'
    CH = {'Authorization': f'Bearer {TOKEN_CF}', 'Content-Type': 'application/json'}
    def d1q(sql, params=None):
        body = json.dumps({'sql': sql, 'params': params or []}).encode('utf-8')
        req = urllib.request.Request(URL, data=body, headers=CH)
        return json.loads(urllib.request.urlopen(req, timeout=30).read())

    r = d1q("UPDATE papers SET body_md = ? WHERE slug = ?",
            [norm, 'ostrowski-dimensionless-reformulation'])
    print(f'D1 update success: {r.get("success")}')
    r2 = d1q("SELECT LENGTH(body_md) as blen FROM papers WHERE slug = ?",
             ['ostrowski-dimensionless-reformulation'])
    print(f'D1 body_md length now: {r2["result"][0]["results"][0]["blen"]}')
else:
    print('D1: no token, skipped')
