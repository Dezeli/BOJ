# 합이 0인 네 정수
import sys

input = sys.stdin.readline

n = int(input())

A, B, C, D = [], [], [], []
for _ in range(n):
    n1, n2, n3, n4 = list(map(int, input().split()))
    A.append(n1)
    B.append(n2)
    C.append(n3)
    D.append(n4)

def solution(A, B, C, D):
    nums = dict()
    
    for i in A:
        for j in B:
            ij = i+j
            nums[ij] = nums.get(ij, 0) + 1
    result = 0
    for i in C:
        for j in D:
            ij = -i-j
            result += nums.get(ij, 0)
    return result

print(solution(A, B, C, D))