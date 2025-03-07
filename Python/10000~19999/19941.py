# 햄버거 분배
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
S = input().rstrip()

ham = [0 for _ in range(N)]

cnt = 0
for i in range(N):
    if S[i]=='H':
        ham[i] = 1

for i in range(N):
    if S[i]=='P':
        for j in range(i-K, i+K+1):
            if j>=N or j<0:
                continue
            if ham[j]==1:
                ham[j] = 0
                cnt += 1
                break
print(cnt)