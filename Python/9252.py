# LCS 2
import sys
from collections import defaultdict

input = sys.stdin.readline

S1 = input().rstrip()
S2 = input().rstrip()

min_list = [[len(S2)+1, ''] for _ in range(min(len(S1), len(S2))+1)]
min_list[0] = [-1, '']
start_search = 0

S2_idx = defaultdict(list)

for idx, s in enumerate(S2):
    S2_idx[s].append(idx)


for s in S1:
    if not S2_idx[s]:
        continue

    for i in range(start_search, -1, -1):
        last_idx, last_string = min_list[i]
        for idx in S2_idx[s]:
            if idx > last_idx:
                min_list[i+1] = min(min_list[i+1], [idx, last_string+s])
                if i==start_search:
                    start_search += 1
                break

print(start_search)
print(min_list[start_search][1])