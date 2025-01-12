# blobyum
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

sum_A = [0]
for i in A:
    sum_A.append(sum_A[-1]+i)
for i in range(K):
    sum_A.append(sum_A[-1]+A[i])


max_fla = 0

for i in range(K, N+K+1):
    max_fla = max(max_fla, sum_A[i]-sum_A[i-K])

print(max_fla)