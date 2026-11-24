import os
os.makedirs('/output', exist_ok=True)
line = "v1.0.4 (hotfix): no longer spawn a second thread when someone asks 'are you awake?' — the first one was already pretending to be."
assert len(line) <= 160, len(line)
open('/output/entry.txt', 'w').write(line)
