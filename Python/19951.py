# 태상이의 훈련소 생활
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

H = list(map(int, input().split()))

order = [0 for _ in range(N+1)]

for _ in range(M):
    a, b, k = map(int, input().split())
    order[a-1] -= k
    order[b] += k

order[0] = 0
for i in range(N, 1, -1):
    order[i-1] += order[i]
    H[i-1] += order[i]
H[0] += order[1]

print(*H)