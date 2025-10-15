# 감시
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

d2 = []
cctvs = []
dir_cctv = {1:[[1], [2], [3], [4]], 2:[[1, 3], [2, 4]], 3:[[1, 2], [2, 3], [3, 4], [4, 1]],
            4:[[1, 2, 3], [2, 3, 4], [3, 4, 1], [4, 1, 2]], 5: [[1, 2, 3, 4]]}

for i in range(N):
    d1 = list(map(int, input().split()))
    for j in range(M):
        if d1[j]!=6 and d1[j]!=0:
            cctvs.append([dir_cctv[d1[j]], i, j])
    d2.append(d1)

len_cctvs = len(cctvs)

def check_blindspot(case):
    blindspot = 0
    for d1 in case:
        blindspot += d1.count(0)
    return blindspot


def cctv_working(dir, x, y, case):
    new_case = [r[:] for r in case]
    
    for d in dir:
        xd, yd = x, y
        while True:
            if d==1:
                xd -= 1
            elif d==2:
                yd += 1
            elif d==3:
                xd += 1
            elif d==4:
                yd -= 1

            if xd >= N or xd<0 or yd>=M or yd<0:
                break
            if new_case[xd][yd]==6:
                break
            if new_case[xd][yd]:
                continue
            else:
                new_case[xd][yd] = -1
    return new_case


min_blindspot = check_blindspot(d2)

def backtrack(depth, case):
    global min_blindspot

    if depth==len_cctvs:
        blindspot = check_blindspot(case)
        min_blindspot = min(min_blindspot, blindspot)
        return
    
    for dir in cctvs[depth][0]:
        backtrack(depth+1, cctv_working(dir, cctvs[depth][1], cctvs[depth][2], case))

backtrack(0, d2)
print(min_blindspot)
