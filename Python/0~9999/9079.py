# 동전 게임
import sys
from collections import deque

input = sys.stdin.readline
T = int(input())


def game(coins):
    visited = [0 for _ in range(512)]
    how = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    ]

    queue = deque([(int(coins, 2), 0)])
    visited[int(coins, 2)] = 1

    while queue:
        coin, cnt = queue.popleft()
        if coin == 0 or coin == 511:
            return cnt
        for h in how:
            new = flip(list(bin(coin)[2:].zfill(9)), h)
            i = int(new, 2)
            if not visited[i]:
                visited[i] = 1
                queue.append((i, cnt + 1))
    return -1


def flip(coin, how):
    for h in how:
        coin[h] = "1" if coin[h] == "0" else "0"
    return "".join(coin)


for _ in range(T):
    board = []
    for i in range(3):
        c = input().split()
        board.append("".join(["1" if ht == "H" else "0" for ht in c]))

    print(game("".join(board)))
