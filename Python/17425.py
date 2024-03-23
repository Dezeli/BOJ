# 약수의 합
import sys

input = sys.stdin.readline

T = int(input())

d = [1 for _ in range(1000000)]
for n in range(2, 1000001):
    for i in range(n, 1000001, n):
        d[i-1] += n

sum_d = [0]
for i in d:
    sum_d.append(sum_d[-1]+i)

for _ in range(T):
    N = int(input())
    print(sum_d[N])
