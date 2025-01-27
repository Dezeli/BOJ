# 박성원
import sys
from math import gcd

input = sys.stdin.readline


N = int(input().strip())
nums = [input().strip() for _ in range(N)]
K = int(input().strip())

mod_nums = []
for num in nums:
    mod_nums.append(int(num) % K)

mod_squares = [1] * 51
for i in range(1, 51):
    mod_squares[i] = (mod_squares[i - 1] * 10) % K

dp = [[0] * K for _ in range(2**N)]
dp[0][0] = 1

for mask in range(2**N):
    for rest in range(K):
        if dp[mask][rest] == 0:
            continue
        for i in range(N):
            if not (mask & (1 << i)):
                new_mask = mask | (1 << i)
                new_rest = (rest * mod_squares[len(nums[i])] + mod_nums[i]) % K
                dp[new_mask][new_rest] += dp[mask][rest]

pos = dp[(1 << N) - 1][0]
case = 1
for i in range(2, N + 1):
    case *= i

if pos == 0:
    print("0/1")
else:
    div = gcd(pos, case)
    print(f"{pos//div}/{case//div}")
