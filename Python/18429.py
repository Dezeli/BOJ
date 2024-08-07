# 근손실
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

case = 0


def fit(over, left):
    global case
    if not left:
        case += 1
        return

    for _ in range(len(left)):
        i = left.pop(0)
        over += i
        over -= K
        if over >= 0:
            fit(over, left)
        over -= i
        over += K
        left.append(i)


fit(0, A)
print(case)
