# 수들의 합 4
import sys
from collections import defaultdict

input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))
S = [0]
for i in range(N):
    S.append(S[-1] + A[i])

ans = 0
sum_dict = defaultdict(int)
for i in range(N, 0, -1):
    sum_num = S[i]
    if sum_num == K:
        ans += 1
    find = sum_num + K
    ans += sum_dict[find]
    sum_dict[sum_num] += 1

print(ans)
