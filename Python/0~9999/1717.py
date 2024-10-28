# 집합의 표현
import sys

sys.setrecursionlimit(10**8)
input = sys.stdin.readline

n, m = map(int, input().split())
nums = [i for i in range(n + 1)]


def find_parent(x):
    if nums[x] != x:
        nums[x] = find_parent(nums[x])
    return nums[x]


def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        nums[b] = a
    else:
        nums[a] = b


for _ in range(m):
    s, a, b = map(int, input().split())
    if s == 0:
        union_parent(a, b)
    else:
        if find_parent(a) == find_parent(b):
            print("YES")
        else:
            print("NO")
