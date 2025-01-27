# 사탕상자
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n = int(input())
max_flavor = 10**6
seg_tree = [0 for _ in range(max_flavor * 4)]


def add_candy(i, l, r, b, c):
    if l <= b <= r:
        seg_tree[i] += c
        if l == b == r:
            return
    else:
        return

    mid = (l + r) // 2
    add_candy(i * 2, l, mid, b, c)
    add_candy(i * 2 + 1, mid + 1, r, b, c)


def pop_candy(i, l, r, b):
    seg_tree[i] -= 1
    if l == r:
        print(l)
        return

    mid = (l + r) // 2
    if seg_tree[i * 2] >= b:
        pop_candy(i * 2, l, mid, b)
    else:
        pop_candy(i * 2 + 1, mid + 1, r, b - seg_tree[i * 2])


for _ in range(n):
    hand = list(map(int, input().split()))
    if hand[0] == 2:
        add_candy(1, 1, max_flavor, hand[1], hand[2])
    else:
        pop_candy(1, 1, max_flavor, hand[1])
