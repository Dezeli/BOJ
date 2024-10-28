# 나는 행복합니다~
import sys

N, M, K = map(int, sys.stdin.readline().split(" "))
print(K // M, K % M)
