# 성 지키기
import sys

N, M = map(int, sys.stdin.readline().split())
nList = [i for i in range(N)]
mList = [i for i in range(M)]
for i in range(N):
    R = sys.stdin.readline().rstrip()
    for j in range(M):
        if R[j] == "X":
            if i in nList:
                nList.remove(i)
            if j in mList:
                mList.remove(j)
print(max([len(nList), len(mList)]))
