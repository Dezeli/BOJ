# 연세워터파크
import sys

input = sys.stdin.readline

sys.setrecursionlimit(10**6)

N, D = map(int, input().split())
K = list(map(int, input().split()))

seg_tree = [0]*(N*4)

def make_tree(l, r, i):
    if l==r:
        seg_tree[i] = K[l]
        return K[l]
    
    mid = (l+r)//2
    seg_tree[i] = max(make_tree(l, mid, i*2), make_tree(mid+1, r, i*2+1))
    return seg_tree[i]

make_tree(0, N-1, 1)

def find_max(l, r, i, a, b):
    if a<=l and r<=b:
        return seg_tree[i]
    if r<a or l>b:
        return -1
    
    mid = (l+r)//2
    return max(find_max(l, mid, i*2, a, b), find_max(mid+1, r, i*2+1, a, b))

def update_max(l, r, i, a, m):
    if a<l or a>r:
        return seg_tree[i]
    if l==r==a:
        seg_tree[i] += m
        return seg_tree[i]

    mid = (l+r)//2
    seg_tree[i] = max(update_max(l, mid, i*2, a, m), update_max(mid+1, r, i*2+1, a, m))
    return seg_tree[i]


for n in range(1, N):
    m = max(0, find_max(0, N-1, 1, n-D, n-1))
    update_max(0, N-1, 1, n, m)

print(seg_tree[1])