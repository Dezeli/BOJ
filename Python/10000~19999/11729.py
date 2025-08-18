# 하노이 탑 이동 순서
import sys

input = sys.stdin.readline

N = int(input())


def move(n, s, e, l):
    if n==1:
        return [[s, e]]

    return move(n-1, s, l, e) + [[s, e]] + move (n-1, l, e, s)


result = move(N, 1, 3, 2)
print(len(result))
for i in result:
    print(*i)