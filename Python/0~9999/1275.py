# 커피숍2
import sys

input = sys.stdin.readline

N, Q = map(int, input().split())
d1 = list(map(int, input().split()))

segment_tree = [0]*(N*4)

def make_tree(s, e, i):
    if s==e:
        segment_tree[i] = d1[s]
        return segment_tree[i]
    
    mid = (s+e)//2
    left = make_tree(s, mid, i*2)
    right = make_tree(mid+1, e, i*2+1)
    segment_tree[i] = left+right

    return segment_tree[i]

make_tree(0, N-1, 1)

def change_tree(s, e, a, b, i):
    if not s<=a<=e:
        return segment_tree[i]

    if s==e:
        segment_tree[i] = b
        return segment_tree[i]

    mid = (s+e)//2
    left = change_tree(s, mid, a, b, i*2)
    right = change_tree(mid+1, e, a, b, i*2+1)
    segment_tree[i] = left + right
    return segment_tree[i]

def get_sum(s, e, x, y, i):
    if y<s or x>e:
        return 0
    elif x<=s and e<=y:
        return segment_tree[i]
    
    mid = (s+e)//2
    left = get_sum(s, mid, x, y, i*2)
    right = get_sum(mid+1, e, x, y, i*2+1)

    return left + right



for _ in range(Q):
    x, y, a, b = map(int, input().split())
    print(get_sum(0, N-1, min(x, y)-1, max(x, y)-1, 1))
    change_tree(0, N-1, a-1, b, 1)