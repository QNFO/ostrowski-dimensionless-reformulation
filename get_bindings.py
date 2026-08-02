import json, sys, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

# Query worker bindings via REST (may work even if content endpoint differs)
import urllib.request
TOKEN = __import__('os').environ.get('CLOUDFLARE_API_TOKEN')
url = 'https://api.cloudflare.com/client/v4/accounts/edb167b78c9fb901ea5bca3ce58ccc4b/workers/scripts/qnfo-gateway/bindings'
req = urllib.request.Request(url, headers={'Authorization': f'Bearer {TOKEN}'})
try:
    r = json.loads(urllib.request.urlopen(req, timeout=20).read())
    print('success:', r.get('success'))
    if r.get('errors'):
        print('errors:', r['errors'])
    for b in r.get('result', []):
        print(f"{b.get('name')}: type={b.get('type')} id={b.get('id','')} namespace={b.get('namespace','')} bucket={b.get('bucket_name','')} database={b.get('database_id','')}")
except Exception as e:
    print(f'ERR: {e}')
