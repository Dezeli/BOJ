# 컬러볼
import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(sys.stdin.readline())
balls = []
for i in range(N):
    c, s = map(int, sys.stdin.readline().split())
    balls.append([c, s, i])

balls.sort(key=lambda x: x[1])

ans = [0 for _ in range(N)]
sum_ball = defaultdict(int)

total = 0
j = 0
for i in range(N):
    while balls[j][1] < balls[i][1]:
        total += balls[j][1]
        sum_ball[balls[j][0]] += balls[j][1]
        j += 1
    ans[balls[i][2]] = total - sum_ball[balls[i][0]]

for i in range(N):
    print(ans[i])
