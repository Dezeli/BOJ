# 피아노 체조
import sys

input = sys.stdin.readline

N = int(input())
level = list(map(int, input().split()))

p_play = [0]

for i in range(N - 1):
    if level[i] > level[i + 1]:
        p_play.append(p_play[-1] + 1)
    else:
        p_play.append(p_play[-1])
p_play.append(p_play[-1])


Q = int(input())
for _ in range(Q):
    s, e = map(int, input().split())
    print(p_play[e - 1] - p_play[s - 1])
