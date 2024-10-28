# 1, 2, 3 더하기
import sys

T = int(sys.stdin.readline().rstrip())


def make_num(plus, n):
    if plus > n:
        return 0
    elif plus == n:
        return 1
    else:
        return make_num(plus + 1, n) + make_num(plus + 2, n) + make_num(plus + 3, n)


for _ in range(T):
    n = int(sys.stdin.readline().rstrip())
    way = make_num(0, n)
    print(way)
