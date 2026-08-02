import re, sys, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

js = open(r'C:\Users\LENOVO\AppData\Local\Temp\odr-inspect\gateway-worker.js', encoding='utf-8').read()

# Find all env.* binding references to build wrangler.toml correctly
env_refs = set(re.findall(r'env\.([A-Z_][A-Z0-9_]*)', js))
print('env bindings referenced:')
for e in sorted(env_refs):
    print(f'  {e}')

# Find routes (URL patterns handled)
print('\nRoute patterns:')
for m in re.finditer(r'pattern:\s*["\']([^"\']+)', js):
    print(f'  {m.group(1)}')

# Check how the worker decides routes
for m in re.finditer(r'url\.hostname|URL\(|pathname|\.pathname', js):
    pass
print('\nTotal JS size:', len(js))
