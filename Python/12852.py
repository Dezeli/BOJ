# 1로 만들기 2
import sys

input = sys.stdin.readline

N = int(input())
dp = [N for _ in range(3*N+1)]
dp[1] = 1

for i in range(1, N):
    dp[i*2] = min(dp[i*2], dp[i]+1)
    dp[i*3] = min(dp[i*3], dp[i]+1)
    dp[i+1] = min(dp[i+1], dp[i]+1)

print(dp[N]-1)
order = [N]
track = N
for _ in range(dp[N]-1):
    if dp[track-1]+1==dp[track]:
        track -= 1
        order.append(track)
    elif track%3==0 and dp[track//3]+1==dp[track]:
        track = track//3
        order.append(track)
    elif track%2==0 and dp[track//2]+1==dp[track]:
        track = track//2
        order.append(track)
print(*order)

