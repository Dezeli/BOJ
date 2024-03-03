# 숨바꼭질
import sys

N, K = map(int, sys.stdin.readline().split(" "))

ran = 200000

times = [0 for _ in range(ran + 1)]

cur = [N]
next = []
time = 0

if N == K:
    print(0)

else:
    while times[K] == False:
        while cur:
            n = cur.pop()
            if n < 0 or n > ran:
                continue
            if times[n]:
                continue
            else:
                times[n] = time
                next += [n - 1, n + 1, n * 2]
        cur = next
        next = []
        time += 1
    print(times[K])
