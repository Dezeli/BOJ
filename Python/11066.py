# 파일 합치기
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    K = int(input())
    files = [0] + list(map(int, input().split()))

    total = [0 for _ in range(K+1)]

    for i in range(1, K+1):
        total[i] = total[i-1] + files[i]

    dp = [[0]*(K+1) for _ in range(K+1)]

    for i in range(2, K+1):
        for j in range(1, K+2-i):
            dp[j][j+i-1] = min([dp[j][j+q] + dp[j+q+1][j+i-1] for q in range(i-1)]) +(total[j+i-1] - total[j-1])
            
    print(dp[1][K])