# 수열과 쿼리 16
import sys

input = sys.stdin.readline

N = int(input())
A = [0] + list(map(int, input().split()))

seg_tree = [0 for _ in range(N * 4)]


def make_tree(l, r, i):
    if l == r:
        seg_tree[i] = [A[l], l]
        return [A[l], l]

    mid = (l + r) // 2
    seg_tree[i] = min(make_tree(l, mid, i * 2), make_tree(mid + 1, r, i * 2 + 1))
    return seg_tree[i]


make_tree(1, N, 1)


def change_tree(l, r, i, t, v):
    if r < t or l > t:
        return seg_tree[i]

    if r == l == t:
        seg_tree[i][0] = v
        return seg_tree[i]

    mid = (l + r) // 2
    seg_tree[i] = min(
        change_tree(l, mid, i * 2, t, v), change_tree(mid + 1, r, i * 2 + 1, t, v)
    )
    return seg_tree[i]


def get_val(l, r, i, t1, t2):
    if r < t1 or l > t2:
        return [10**9 + 1, 0]

    if t1 <= l and r <= t2:
        return seg_tree[i]

    mid = (l + r) // 2
    return min(get_val(l, mid, i * 2, t1, t2), get_val(mid + 1, r, i * 2 + 1, t1, t2))


M = int(input())
for _ in range(M):
    a, b, c = map(int, input().split())
    if a == 1:
        change_tree(1, N, 1, b, c)
    else:
        print(get_val(1, N, 1, b, c)[1])
