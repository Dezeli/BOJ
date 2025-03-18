# 이장님 초대
import sys

input = sys.stdin.readline

N = int(input())
t = list(map(int, input().split()))
t.sort(reverse=True)

max_time = 0

for i in range(N):
    max_time = max(max_time, t[i] + i + 2)

print(max_time)
