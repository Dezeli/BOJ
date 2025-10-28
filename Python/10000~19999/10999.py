# 구간 합 구하기 2
import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())
data = list(map(int, sys.stdin.read().split()))
nums = [0] + data[:N]
segment_tree = [0]*(N*4)
lazy_tree = [0]*(N*4)

def make_tree(s, e, i):
    if s==e:
        segment_tree[i] = nums[s]
        return segment_tree[i]
    
    mid = (s+e)//2
    left = make_tree(s, mid, i*2)
    right = make_tree(mid+1, e, i*2+1)
    segment_tree[i] = left + right
    return segment_tree[i]

make_tree(1, N, 1)

def lazy_update(s, e, b, c, d, i):
    if e<b or s>c:
        return
    if b<=s and e<=c:
        lazy_tree[i] += d
        return

    mid = (s+e)//2
    lazy_update(s, mid, b, c, d, i*2)
    lazy_update(mid+1, e, b, c, d, i*2+1)
    return

def change_tree(s, e, b, c, d, i):
    if e<b or s>c:
        lazy_tree[i] = d
        return
    if s==e:
        segment_tree[i] += d
        return segment_tree[i]

    mid = (s+e)//2
    left = change_tree(s, mid, b, c, d + lazy_tree[i], i*2)
    right = change_tree(mid+1, e, b, c, d + lazy_tree[i], i*2+1)
    segment_tree[i] = left + right
    return segment_tree[i]

def get_sum(s, e, b, c, i):
    if e<b or s>c:
        return 0
    
    if lazy_tree[i]:
        change_tree(s, e, b, c, 0, i)
        lazy_tree[i]= 0
        
    if s>=b and e<=c:
        return segment_tree[i]
    
    mid = (s+e)//2
    left = get_sum(s, mid, b, c, i*2)
    right = get_sum(mid+1, e, b, c, i*2+1)
    return left+right

queries = data[N:]
idx = 0
for _ in range(M + K):
    t = queries[idx]
    idx += 1
    if t == 1:
        b, c, d = queries[idx], queries[idx+1], queries[idx+2]
        idx += 3
        change_tree(1, N, b, c, d, 1)
    else:
        b, c = queries[idx], queries[idx+1]
        idx += 2
        print(get_sum(1, N, b, c, 1))