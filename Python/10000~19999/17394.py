# 핑거 스냅
import sys

input = sys.stdin.readline

T = int(input())

limit = 100001
isPrime = [0] * limit

for i in range(2, int(limit ** (1 / 2)) + 1):
    if isPrime[i] == 0:
        for j in range(2 * i, limit, i):
            isPrime[j] = 1


def prime(m, n):
    p = []
    for i in range(m, n + 1):
        if i > 1 and isPrime[i] == 0:
            p.append(i)
    return p


for _ in range(T):
    N, A, B = map(int, input().split())
    p = prime(A, B)
    if not p:
        print(-1)
        continue

    queue = [N]
    visit = [0 for _ in range(1000001)]
    cnt = 0
    nQueue = []
    while True:
        if not queue:
            if nQueue:
                cnt += 1
                queue += nQueue
                nQueue = []
            else:
                print(-1)
                break
        num = queue.pop()
        if num in p:
            print(cnt)
            break
        if num > 1000000 or num < 0:
            continue
        if visit[num] == 1:
            continue

        visit[num] = 1
        nQueue += [num // 2, num // 3, num + 1, num - 1]
