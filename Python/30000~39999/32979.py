# 아파트
import sys

input = sys.stdin.readline

N = int(input()) * 2

T = int(input())

apt = list(map(int, input().split()))
shout = list(map(int, input().split()))

ans = []

cur = -1
for i in shout:
    cur += i % N
    if cur >= N:
        cur -= N
    ans.append(apt[cur])
    cur -= 1

print(*ans)
