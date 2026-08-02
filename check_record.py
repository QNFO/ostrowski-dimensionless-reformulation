import urllib.request, json

# Check what's actually published at 21755771 (the v4.0.2 record)
r = json.loads(urllib.request.urlopen('https://zenodo.org/api/records/21755771').read())
print('ID:', r['id'])
print('Version:', r['metadata'].get('version'))
print('Created:', r['created'])
print('Files:')
for f in r.get('files', []):
    print(f"  {f['key']} ({f['size']} bytes)")
print('is_last:', r['metadata']['relations']['version'][0].get('is_last'))
