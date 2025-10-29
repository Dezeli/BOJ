# 구간 합 구하기 2
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M, K = map(int, input().split())
data = list(map(int, sys.stdin.read().split()))

nums = [0] + data[:N]
queries = data[N:]

segment_tree = [0] * (N * 4)
lazy_tree = [0] * (N * 4)

def build(node, start, end):
    if start == end:
        segment_tree[node] = nums[start]
        return segment_tree[node]
    mid = (start + end) // 2
    segment_tree[node] = build(node*2, start, mid) + build(node*2+1, mid+1, end)
    return segment_tree[node]

def propagate(node, start, end):
    if lazy_tree[node] != 0:
        segment_tree[node] += (end - start + 1) * lazy_tree[node]
        if start != end:
            lazy_tree[node*2] += lazy_tree[node]
            lazy_tree[node*2+1] += lazy_tree[node]
        lazy_tree[node] = 0

def update(node, start, end, left, right, diff):
    propagate(node, start, end)
    if end < left or start > right:
        return
    if left <= start and end <= right:
        segment_tree[node] += (end - start + 1) * diff
        if start != end:
            lazy_tree[node*2] += diff
            lazy_tree[node*2+1] += diff
        return
    mid = (start + end) // 2
    update(node*2, start, mid, left, right, diff)
    update(node*2+1, mid+1, end, left, right, diff)
    segment_tree[node] = segment_tree[node*2] + segment_tree[node*2+1]

def query(node, start, end, left, right):
    propagate(node, start, end)
    if end < left or start > right:
        return 0
    if left <= start and end <= right:
        return segment_tree[node]
    mid = (start + end) // 2
    return query(node*2, start, mid, left, right) + query(node*2+1, mid+1, end, left, right)

build(1, 1, N)

idx = 0
out = []
for _ in range(M + K):
    t = queries[idx]
    idx += 1
    if t == 1:
        b, c, d = queries[idx], queries[idx+1], queries[idx+2]
        idx += 3
        update(1, 1, N, b, c, d)
    else:
        b, c = queries[idx], queries[idx+1]
        idx += 2
        print(query(1, 1, N, b, c))
