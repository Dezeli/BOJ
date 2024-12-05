# 최솟값과 최댓값

N, M = map(int, input().split())

nums = [int(input()) for _ in range(N)]

min_tree = [0 for _ in range(N * 4)]
max_tree = [0 for _ in range(N * 4)]


def make_tree(l, r, i):
    if l == r:
        min_tree[i] = nums[l]
        max_tree[i] = nums[l]
        return nums[l], nums[l]

    mid = (l + r) // 2
    min1, max1 = make_tree(l, mid, i * 2)
    min2, max2 = make_tree(mid + 1, r, i * 2 + 1)
    min_tree[i] = min(min1, min2)
    max_tree[i] = max(max1, max2)
    return min_tree[i], max_tree[i]


make_tree(0, N - 1, 1)

max_limit = 10**9
min_limit = 1


def get_val(l, r, i, a, b):
    if a <= l and r <= b:
        return min_tree[i], max_tree[i]
    if (a < l and b < l) or (a > r and b > r):
        return max_limit, min_limit

    mid = (l + r) // 2
    min1, max1 = get_val(l, mid, i * 2, a, b)
    min2, max2 = get_val(mid + 1, r, i * 2 + 1, a, b)
    return min(min1, min2), max(max1, max2)


for _ in range(M):
    a, b = map(int, input().split())
    print(*get_val(0, N - 1, 1, a - 1, b - 1))
