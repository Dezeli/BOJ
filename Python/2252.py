# 줄 세우기
import sys
from collections import defaultdict

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())

order = defaultdict(list)
check = [False for _ in range(N+1)]
right_order = []

for _ in range(M):
    A, B = map(int, input().split())
    order[B].append(A)

def make_line(n):
    for i in order[n]:
        if check[i]:
            continue
        make_line(i)
        check[i] = True
    right_order.append(n)
    check[n] = True

for i in range(1, N+1):
    if check[i]:
        continue
    make_line(i)

print(*right_order)