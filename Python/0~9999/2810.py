# 컵홀더
import sys

input = sys.stdin.readline

N = int(input())

S = input().rstrip()

cnt1 = S.split("LL")
cnt2 = []

for i in cnt1:
    cnt2 += i.split("S")

print(min(len(cnt2), N))
