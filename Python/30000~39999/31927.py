# 렬정! 렬정! 렬정!
import sys

input = sys.stdin.readline

K = int(input())
A = list(map(int, input().split()))

print(K // 2)
for i in range(K // 2):
    A[0 + i] += 5001 * ((K // 2) - i)
    A[-1 - i] -= 5001 * ((K // 2) - i)
    print(*A)
