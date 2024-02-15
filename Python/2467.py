# 용액
import sys

input = sys.stdin.readline

N = int(input())
liquids = list(map(int, input().split()))

l = 0
r = N - 1

min_sum = abs(liquids[l] + liquids[r])
ans = [[liquids[l], liquids[r]]]

while l < r:
    case = liquids[l] + liquids[r]

    if abs(case) < min_sum:
        ans.append([liquids[l], liquids[r]])
        min_sum = abs(case)
        if min_sum == 0:
            break
    
    if case < 0:
        l += 1
    else:
        r -= 1

print(*ans[-1])