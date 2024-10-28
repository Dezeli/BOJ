# 트로피 진열
import sys

N = int(sys.stdin.readline().rstrip())

trophies = []
for _ in range(N):
    trophies.append(int(sys.stdin.readline().rstrip()))
for _ in range(2):
    cnt = 1
    max_h = trophies[0]
    for i in range(1, len(trophies)):
        if max_h < trophies[i]:
            max_h = trophies[i]
            cnt += 1
    trophies.reverse()
    print(cnt)
