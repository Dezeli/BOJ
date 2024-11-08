# 웰컴 키트
import sys

input = sys.stdin.readline

N = int(input())

sizes = list(map(int, input().split()))

T, P = map(int, input().split())

tshirts = 0
for i in sizes:
    tshirts += i // T
    if i % T > 0:
        tshirts += 1

print(tshirts)
print(*divmod(N, P))
