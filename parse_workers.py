import json, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
r = json.load(open(r'C:\Users\LENOVO\AppData\Local\Temp\odr-inspect\workers-list.json', encoding='utf-8'))
print('success:', r.get('success'))
if r.get('errors'):
    print('errors:', r['errors'])
for w in r.get('result', []):
    print(w.get('id'), '|', w.get('modified_on', '')[:19])
