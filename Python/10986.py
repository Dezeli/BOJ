# 나머지 합
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

A = list(map(int, input().split()))

left = [0]*M
sum_num = 0
for i in range(N):
    sum_num += A[i]
    left[sum_num%M] += 1

ans = left[0]
for i in range(M):
    ans += left[i]*(left[i]-1)//2
print(ans)