# Maximum Subarray
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    X = list(map(int, input().split()))

    sum_X = [0]
    for i in X:
        sum_X.append(sum_X[-1] + i)

    max_sum = -3000
    for i in range(N+1):
        for j in range(i+1, N+1):
            max_sum = max(sum_X[j]-sum_X[i], max_sum)
    print(max_sum)