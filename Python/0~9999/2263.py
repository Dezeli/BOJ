# 트리의 순회
import sys

input = sys.stdin.readline

sys.setrecursionlimit(10**5)

n = int(input())
inord = list(map(int, input().split()))[::-1]
postord = list(map(int, input().split()))[::-1]

preord = []

def find(s1, e1, s2, e2):
    next = []
    cnt = 0
    while s1<=e1 and s2<=e2:
        if postord[s2]==inord[s1]:
            preord.append(inord[s1])
            if cnt!=0:
                next.append([s1-cnt, s1-1, s2+1, s2+cnt])
            s2 += cnt+1
            cnt = -1
        s1 += 1
        cnt += 1

    for l in next[::-1]:
        find(*l)

    return

find(0, n-1, 0, n-1)
print(*preord)