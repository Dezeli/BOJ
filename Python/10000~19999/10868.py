# 최솟값
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

nums = [int(input()) for _ in range(N)]

seg_tree = [0]*(N*4)

def make_tree(i, x, y):
    if x==y:
        seg_tree[i] = nums[x]
        return seg_tree[i]

    mid = (x+y)//2
    seg_tree[i] = min(make_tree(i*2, x, mid), make_tree(i*2+1, mid+1, y))
    return seg_tree[i]

make_tree(1, 0, N-1)


def find_min(i, x, y, a, b):
    if x>=a and y<=b:
        return seg_tree[i]
    
    if y<a or x>b:
        return 10**9

    mid = (x+y)//2
    return min(find_min(i*2, x, mid, a, b), find_min(i*2+1, mid+1, y, a, b))

for _ in range(M):
    a, b = map(int, input().split())
    print(find_min(1, 0, N-1, a-1, b-1))