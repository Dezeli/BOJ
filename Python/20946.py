# 합성인수분해
import sys

input = sys.stdin.readline

N = int(input())


def sol(n):
    k = 2
    result = []
    cnt = 0
    while n > 1:
        if n % k == 0:
            if cnt % 2 == 0:
                result.append(k)
            else:
                result[-1] *= k
            cnt += 1
            n //= k
            continue
        k += 1
        if n ** (1 / 2) < k:
            if cnt % 2 == 0:
                result.append(n)
            else:
                result[-1] *= n
            cnt += 1
            break
    if cnt % 2 == 1 and cnt >= 3:
        n = result.pop()
        result[-1] *= n
    if cnt == 1:
        return [-1]
    return result


result = sol(N)
print(*result)
