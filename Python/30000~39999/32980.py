# 분리배출
import sys

input = sys.stdin.readline

N = int(input())

dust = [input().rstrip() for _ in range(N)]

P, C, V, S, G, F = map(int, input().split())
O = int(input())
P = min(P, O)
C = min(C, O)
V = min(V, O)
S = min(S, O)
G = min(G, O)
F = min(F, O)

cnt = 0

for d in dust:
    if d[0] == "O":
        cnt += len(d) * O
    else:
        if d.count(d[0]) == len(d):
            if d[0] == "P":
                cnt += len(d) * P
            elif d[0] == "C":
                cnt += len(d) * C
            elif d[0] == "V":
                cnt += len(d) * V
            elif d[0] == "S":
                cnt += len(d) * S
            elif d[0] == "G":
                cnt += len(d) * G
            else:
                cnt += len(d) * F
        else:
            cnt += len(d) * O
print(cnt)
