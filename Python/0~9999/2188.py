# 축사 배정
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())

want = [[]]

for _ in range(N):
    d1 = list(map(int, input().split()))
    want.append(d1[1:])


rooms = [0 for _ in range(M+1)]
def get_room(n):
    for i in want[n]:
        if visit[i]:
            continue
        visit[i] = 1

        if rooms[i]==0:
            rooms[i] = n
            return True
        else:
            if get_room(rooms[i]):
                rooms[i] = n
                return True
    return False


cnt = 0

for n in range(1, N+1):
    visit = [0]*(M+1)
    if get_room(n):
        cnt += 1
print(cnt)