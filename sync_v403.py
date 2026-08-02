import json, urllib.request, os

NEW_DOI = '10.5281/zenodo.21755880'
NEW_ID = 21755880
PAPER_DIR = os.path.expandvars(r'%TEMP%\odr-inspect')
SLUG = 'ostrowski-dimensionless-reformulation'
TOKEN_CF = os.environ.get('CLOUDFLARE_API_TOKEN')

# 1. Paper YAML
paper_path = f'{PAPER_DIR}\\{SLUG}.md'
with open(paper_path, 'r', encoding='utf-8') as f:
    paper = f.read()
paper = paper.replace('doi: "10.5281/zenodo.21755771"', f'doi: "{NEW_DOI}"')
paper = paper.replace('version: "4.0.2"', 'version: "4.0.3"')
paper = paper.replace('v4.0.2: A Place-Democratic', 'v4.0.3: A Place-Democratic')
paper = paper.replace('Reformulation v4.0.2:', 'Reformulation v4.0.3:')
with open(paper_path, 'w', encoding='utf-8') as f:
    f.write(paper)
print(f'1. Paper YAML: DOI={NEW_DOI}, v4.0.3 ({len(paper)} chars)')

# 2. .zenodo_versions.json
vp = f'{PAPER_DIR}\\.zenodo_versions.json'
with open(vp, 'r', encoding='utf-8') as f:
    vs = json.load(f)
vs['latest_deposit_id'] = NEW_ID
vs['versions'].append({"doi": NEW_DOI, "deposit_id": NEW_ID, "tag": "v4.0.3", "published_at": "2026-08-02"})
with open(vp, 'w', encoding='utf-8') as f:
    json.dump(vs, f, indent=2)
print(f'2. .zenodo_versions.json: {len(vs["versions"])} versions, latest={NEW_ID}')

# 3. D1
if TOKEN_CF:
    ACCOUNT = 'edb167b78c9fb901ea5bca3ce58ccc4b'
    DB = '70a58cb3-b2cd-498d-877f-ecca86859a22'
    URL = f'https://api.cloudflare.com/client/v4/accounts/{ACCOUNT}/d1/database/{DB}/query'
    CH = {'Authorization': f'Bearer {TOKEN_CF}', 'Content-Type': 'application/json'}
    def d1q(sql, params=None):
        body = json.dumps({'sql': sql, 'params': params or []}).encode('utf-8')
        req = urllib.request.Request(URL, data=body, headers=CH)
        return json.loads(urllib.request.urlopen(req, timeout=30).read())
    d1q("UPDATE papers SET doi = ?, body_md = ?, version = ? WHERE slug = ?", [NEW_DOI, paper, '4.0.3', SLUG])
    r = d1q("SELECT doi, version, LENGTH(body_md) as blen FROM papers WHERE slug = ?", [SLUG])
    row = r['result'][0]['results'][0]
    ok = row['doi'] == NEW_DOI and row['version'] == '4.0.3'
    print(f'3. D1: DOI={row["doi"]}, version={row["version"]}, blen={row["blen"]}')
    print(f'   {"SYNCED OK" if ok else "MISMATCH!"}')
else:
    print('3. D1: SKIPPED (no token)')

print(f'\nAll synced to {NEW_DOI}')
