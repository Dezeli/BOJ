# 적록색약
from sys import stdin

N = int(stdin.readline().rstrip())

origin = []
change = []
for _ in range(N):
    line = (stdin.readline().rstrip())
    origin.append(list(line))
    change.append(list('G' if i=='R' else i for i in line))

def DFS(picture):
    cnt = 0
    checked = [0 for _ in range(N*N)]
    while sum(checked)!=N*N:
        firsty, firstx = divmod(checked.index(0), N)
        cnt += 1
        color = picture[firsty][firstx]
        queue = [[firstx, firsty]]
        while queue:
            x, y = queue.pop()
            if x<0 or x>=N:
                continue
            if y<0 or y>=N:
                continue
            if picture[y][x]!=color:
                continue
            if checked[y*N+x]==1:
                continue

            checked[y*N+x] = 1
            queue += [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]

    return cnt

print(DFS(origin), DFS(change))