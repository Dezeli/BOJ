# LCS
import sys
from collections import defaultdict

input = sys.stdin.readline

str2_idx = defaultdict(list)

str1 = input().rstrip()
str2 = input().rstrip()
len_str = max([len(str1), len(str2)])

for idx, s in enumerate(str2):
    str2_idx[s].append(idx)

max_cnt = {}
for i in range(1, len_str + 1):
    max_cnt[i] = len_str + 1
max_cnt[0] = -1

for idx, s in enumerate(str1):
    if not str2_idx[s]:
        continue
    for key in range(idx + 1, -1, -1):
        val = max_cnt[key]
        if val == len_str + 1:
            continue
        for i in str2_idx[s]:
            if i > val:
                max_cnt[key + 1] = min([max_cnt[key + 1], i])
                break

for i in range(len_str, 0, -1):
    if max_cnt[i] < len_str:
        print(i)
        break

if max_cnt[1] == len_str + 1:
    print(0)
