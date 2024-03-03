# 골롱 수열
import sys

n = int(sys.stdin.readline().rstrip())


def golomb():
    suyeol = [(0, 0), (1, 1), (2, 3), (4, 5)]
    idx = 3
    last = 5
    while True:
        start, end = suyeol[idx]
        for _ in range(start, end + 1):
            if last + 1 <= n <= last + idx:
                return len(suyeol)
            suyeol.append((last + 1, last + idx))
            last += idx
        idx += 1


if n == 1:
    result = 1
elif n == 2 or n == 3:
    result = 2
else:
    result = golomb()
print(result)
