# 팰린드롬 분할
import sys

input = sys.stdin.readline

S = input().rstrip()
N = len(S)

palindrome = [[0]*N for _ in range(N)]
DP = [2500]*(N+1)
DP[-1] = 0


for j in range(N):
    for i in range(j+1):
        if S[i]==S[j] and (j-i<2 or palindrome[i+1][j-1]):
            palindrome[i][j] = 1
            DP[j] = min(DP[j], DP[i-1]+1)

print(DP[N-1])