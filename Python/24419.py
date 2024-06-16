# 알고리즘 수업 - 행렬 경로 문제 2
import sys
from math import factorial

input = sys.stdin.readline

n = int(input())

board = [list(map(int, input().split())) for _ in range(5)]

print(factorial(2*n) // (factorial(n)**2) % 1000000007, n**2)