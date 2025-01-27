# 아 맞다 마늘
import sys

input = sys.stdin.readline

N = int(input())

mat1 = set(input().rstrip().split())
mat2 = set(input().rstrip().split())

mat3 = mat1 - mat2
print(*mat3)
