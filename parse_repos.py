import json, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
r = json.load(open(r'C:\Users\LENOVO\AppData\Local\Temp\odr-inspect\qnfo-repos.json', encoding='utf-8'))
print(f'Total repos: {len(r)}')
for repo in r:
    name = repo.get('name', '')
    print(f"{name} | {repo.get('pushed_at','')[:10]} | {(repo.get('description') or '')[:50]}")
