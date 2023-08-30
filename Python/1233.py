# Bovine Bones
import sys
from collections import defaultdict

S1, S2, S3 = map(int, sys.stdin.readline().split())
num_Dict = defaultdict(int)
for i1 in range(1, S1 + 1):
    for i2 in range(1, S2 + 1):
        for i3 in range(1, S3 + 1):
            num_Dict[i1 + i2 + i3] += 1
print(max(num_Dict, key=num_Dict.get))
