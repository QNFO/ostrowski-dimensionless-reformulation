import re, sys

text = open(r'C:\Users\LENOVO\AppData\Local\Temp\odr-inspect\ostrowski-dimensionless-reformulation.md', encoding='utf-8').read()
lines = text.splitlines()

keywords = ['overclaim', 'p-adic', 'CAN BE', 'first principle', 'predict', 'discover', 'speculative', 'CALIBRATION', 'v2.0', 'red-team', 'limitation', 'numerolog', 'sigma', 'p-value', 'post-hoc', 'ontology', 'manifesto', 'honesty', 'correct', 'acknowledge', 'claim']

for i, line in enumerate(lines):
    for kw in keywords:
        if kw.lower() in line.lower():
            print(f'KW={kw} | L{i+1}: {line.strip()[:250]}')
            sys.stdout.flush()
