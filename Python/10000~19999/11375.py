# 열혈강호
import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N, M = map(int, input().split())

can_work = [[] for _ in range(N+1)]
jobs = [0]*(M+1)

for i in range(1, N+1):
    d1 = list(map(int, input().split()))
    can_work[i] = d1[1:]

def get_next_jobs(i):
    for j in can_work[i]:
        if visit[j]:
            continue
        visit[j] = True
        if jobs[j] == 0 or get_next_jobs(jobs[j]):
            jobs[j] = i
            return True
    return False

cnt = 0
for i in range(1, N+1):
    visit = [False]*(M+1)
    if get_next_jobs(i):
        cnt += 1
print(cnt)