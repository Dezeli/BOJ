# Skarpetki 
from collections import defaultdict

socks = defaultdict(int)
S = input()

for i in S:
    socks[i] += 1

cnt = 0

for val in socks.values():
    cnt += val//2
print(cnt)