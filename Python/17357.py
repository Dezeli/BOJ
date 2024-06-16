# 자동차가 차주 김표준의 편을 들면?
import sys
import math

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
sum_A = [0]
for i in A:
    sum_A.append(sum_A[-1]+i)

for i in range(1, N+1):
    max_std = 0
    ans = 0
    for j in range(N-i+1):
        mean = (sum_A[j+i]-sum_A[j])/i
        vsum = 0
        for val in A[j:j+i]:
            vsum += (val - mean)**2
        variance = vsum/i
        std = round(math.sqrt(variance), 9)
        if max_std < std:
            max_std = std
            ans = j
    print(ans+1)
