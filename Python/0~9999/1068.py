# 트리
import sys

input = sys.stdin.readline

N = int(input())

p = list(map(int, input().split()))
e = int(input())

leaf = [1] * N

for i in range(N):
    if p[i] == -1:
        leaf[i] = 0
    else:
        leaf[p[i]] = 0


def find(i):
    global cnt
    if p[i] == -1:
        return
    elif p[i] == e:
        cnt += 1
        return
    find(p[i])


cnt = 0
for i in range(N):
    if leaf[i] == 1:
        if i == e:
            cnt += 1
        find(i)

if p.count(p[e]) <= 1 and p[e] != -1:
    cnt -= 1

# print(leaf)
print(sum(leaf) - cnt)
