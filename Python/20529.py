# 가장 가까운 세 사람의 심리적 거리
from sys import stdin
from itertools import combinations

T = int(stdin.readline().rstrip())

def distance(A, B, C):
    d = 0
    for i in range(4):
        if A[i]!=B[i]:
            d += 1
        if A[i]!=C[i]:
            d += 1
        if B[i]!=C[i]:
            d += 1
    return d

for _ in range(T):
    N = int(stdin.readline().rstrip())
    mbti_list = list(stdin.readline().split(" "))

    if N>32:
        print(0)
        continue

    print(min([distance(a, b, c) for a, b, c in combinations(mbti_list, 3)]))
        