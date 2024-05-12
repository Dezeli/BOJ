# 귀찮아 (SIB)
import sys

input = sys.stdin.readline

n = int(input())
x = list(map(int, input().split()))

pSum = [x[0]]
for i in range(1, n):
    pSum.append(pSum[i - 1] + x[i])

ans = 0
for i in range(n - 1):
    ans += x[i] * (pSum[n - 1] - pSum[i])

print(ans)
