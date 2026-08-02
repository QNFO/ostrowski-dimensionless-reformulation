text = open(r'C:\Users\LENOVO\AppData\Local\Temp\odr-inspect\ostrowski-dimensionless-reformulation.md', encoding='utf-8').read()
lines = text.splitlines()

# Extract key sections for reputation audit
sections = [
    ('Limitations', 648, 660),
    ('What Reformulation Does Not Change', 613, 648),
    ('Conclusion', 656, 695),
    ('Research Roadmap', 674, 830),
    ('Declarations', 1152, 1200),
    ('Calibration Register', 1136, 1155),
    ('Compton Counts / Physics Is Rational', 288, 320),
    ('Breadth Trap', 248, 270),
    ('Core Refinements / Prior Overclaims', 1, 40),
    ('Discussion (full)', 611, 660),
    ('Comparative Analysis', 619, 650),
    ('Final So What', 803, 830),
    ('Boundary Cases', 638, 652),
]

for name, start, end in sections:
    with open(rf'C:\Users\LENOVO\AppData\Local\Temp\odr-inspect\section_{name.replace(" ", "_").replace("/", "_")}.txt', 'w', encoding='utf-8') as f:
        for i in range(max(0, start-1), min(end, len(lines))):
            f.write(f"L{i+1}: {lines[i]}\n")

print('done')
