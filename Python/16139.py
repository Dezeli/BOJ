# 인간-컴퓨터 상호작용
import sys

input = sys.stdin.readline

S = input().rstrip()

alps = [[0 for _ in range(26)]]
cur = [0 for _ in range(26)]

for i in S:
    cur[ord(i) - 97] += 1
    alps.append(cur[:])

q = int(input())
for _ in range(q):
    a, l, r = input().rstrip().split()
    print(alps[int(r) + 1][ord(a) - 97] - alps[int(l)][ord(a) - 97])
