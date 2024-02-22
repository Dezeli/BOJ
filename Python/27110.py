# 특식 배부

N = int(input())

A, B, C = map(int, input().split())

print(min(N, A) + min(N, B) + min(N, C))