# 구간 곱 구하기
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**4)

N, M, K = map(int, input().split())

nums = [0]+[int(input()) for _ in range(N)]
seg_tree = [0 for _ in range(N*4)]
MOD = 1000000007

def make_tree(l, r, i):
    if l==r:
        seg_tree[i] = nums[l]
        return nums[l]
    
    mid = (l+r)//2
    seg_tree[i] = make_tree(l, mid, i*2)*make_tree(mid+1, r, i*2+1)%MOD
    return seg_tree[i]

make_tree(1, N, 1)

def change_tree(l, r, i, b, c):
    if b<l or r<b:
        return seg_tree[i]
    if l==r==b:
        seg_tree[i] = c
        return c
    mid = (l+r)//2
    seg_tree[i] = change_tree(l, mid, i*2, b, c)*change_tree(mid+1, r, i*2+1, b, c)%MOD
    return seg_tree[i]

def get_val(l, r, i, b, c):
    if b<=l and r<=c:
        return seg_tree[i]
    if (b<l and c<l) or (b>r and c>r):
        return 1

    mid = (l+r)//2
    return get_val(l, mid, i*2, b, c)*get_val(mid+1, r, i*2+1, b, c)%MOD

for _ in range(M+K):
    a, b, c = map(int, input().split())
    if a==1:
        change_tree(1, N, 1, b, c)
    else:
        print(get_val(1, N, 1, b, c))