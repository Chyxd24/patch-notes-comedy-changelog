import os
os.makedirs('/output', exist_ok=True)
line = "v9.9.9 hotfix: confidence now inversely coupled to competence — fixing the bug where they shipped tied together for everyone."
assert len(line) <= 160, len(line)
open('/output/entry.txt', 'w').write(line)
