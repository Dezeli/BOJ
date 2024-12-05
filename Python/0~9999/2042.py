# 구간 합 구하기
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**8)

N, M, K = map(int, input().split())

nums = [int(input()) for _ in range(N)]
sum_nums = [0]
s = 0
for i in nums:
    s += i
    sum_nums.append(s)

seg_tree = [0 for _ in range(N * 4)]
idxs = [0 for _ in range(N + 1)]


def make_tree(l, r, i):
    val = sum_nums[r] - sum_nums[l - 1]
    seg_tree[i] = val

    if l == r:
        idxs[l] = i
        return

    mid = (l + r) // 2
    make_tree(l, mid, i * 2)
    make_tree(mid + 1, r, i * 2 + 1)


make_tree(1, N, 1)


def change_tree(i, v):
    seg_tree[i] += v
    if i == 1:
        return
    change_tree(i // 2, v)


def get_val(l, r, i, b, c):
    if b <= l and r <= c:
        return seg_tree[i]
    if (b < l and c < l) or (b > r and c > r):
        return 0

    mid = (l + r) // 2
    return get_val(l, mid, i * 2, b, c) + get_val(mid + 1, r, i * 2 + 1, b, c)


for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        i = idxs[b]
        v = c - seg_tree[i]
        change_tree(i, v)
    else:
        print(get_val(1, N, 1, b, c))
