# Dance Dance Revolution
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def move(s, d):
    if s == d:
        return 1
    elif s == 0:
        return 2
    elif abs(d - s) == 2:
        return 4
    else:
        return 3


def solve(n, l, r):
    global dp
    if n >= len(order) - 1:
        return 0

    if dp[n][l][r] != -1:
        return dp[n][l][r]

    dp[n][l][r] = min(
        solve(n + 1, order[n], r) + move(l, order[n]),
        solve(n + 1, l, order[n]) + move(r, order[n]),
    )
    return dp[n][l][r]


order = list(map(int, input().split()))
dp = [[[-1] * 5 for _ in range(5)] for _ in range(100000)]

print(solve(0, 0, 0))
