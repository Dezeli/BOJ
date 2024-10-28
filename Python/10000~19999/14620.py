# 꽃길
import sys
from itertools import combinations

input = sys.stdin.readline


def check(li):
    visited = []
    total = 0
    for r, c in li:
        visited.append((r, c))
        total += dirts[r][c]
        for idx in range(4):
            nr = r + d[idx][0]
            nc = c + d[idx][1]
            if (nr, nc) not in visited:
                visited.append((nr, nc))
                total += dirts[nr][nc]
            else:
                return int(1e9)
    return total


d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

N = int(input())
ans = int(1e9)
dirts = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
can = [(r, c) for r in range(1, N - 1) for c in range(1, N - 1)]

for com in combinations(can, 3):
    ans = min(ans, check(com))
print(ans)
