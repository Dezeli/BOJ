# ∑|ΔEasyMAX|
import sys

input = sys.stdin.readline

N, Q = map(int, input().split())

a = list(map(int, input().split()))
sum_a = [0]

for i in range(N - 1):
    sum_a.append(sum_a[-1] + abs(a[i] - a[i + 1]))

for _ in range(Q):
    s, e = map(int, input().split())
    print(sum_a[e - 1] - sum_a[s - 1])
