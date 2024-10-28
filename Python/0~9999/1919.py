# 애너그램 만들기
from collections import defaultdict

w1 = defaultdict(int)
w2 = defaultdict(int)

for i in input():
    w1[i] += 1

for i in input():
    w2[i] += 1

cnt = 0
for key, val in w1.items():
    cnt += abs(val - w2[key])

for key, val in w2.items():
    if w1[key] == 0:
        cnt += val

print(cnt)
