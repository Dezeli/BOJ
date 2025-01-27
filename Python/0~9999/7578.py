# 공장
import sys

input = sys.stdin.readline


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
o = {B[i]: i + 1 for i in range(N)}
oA = [0] + [o[i] for i in A]
seg_tree = [0] * (N * 4)


def get_cnt(i, l, r, a, b):
    if a <= l <= r <= b:
        return seg_tree[i]
    if b < l or r < a:
        return 0

    mid = (l + r) // 2
    return get_cnt(i * 2, l, mid, a, b) + get_cnt(i * 2 + 1, mid + 1, r, a, b)


def update_tree(i, l, r, t):
    if l <= t <= r:
        seg_tree[i] += 1
    else:
        return
    if l == r:
        return

    mid = (l + r) // 2
    update_tree(i * 2, l, mid, t)
    update_tree(i * 2 + 1, mid + 1, r, t)


cnt = 0
for i in range(1, N + 1):
    cnt += get_cnt(1, 1, N, oA[i], N)
    update_tree(1, 1, N, oA[i])

print(cnt)
