# 스타트와 링크
import sys

input = sys.stdin.readline

N = int(input())

ability = [list(map(int, input().split())) for _ in range(N)]

min_dif = 10**8

def dfs(member):
    global min_dif
    if len(member)==N//2:
        left = [i for i in range(N)]
        for i in member:
            left.remove(i)
    
        team1 = 0
        team2 = 0
        for i in range(N//2):
            for j in range(N//2):
                team1 += ability[member[i]][member[j]]
                team2 += ability[left[i]][left[j]]
        
        min_dif = min(min_dif, abs(team1-team2))
        return
    
    if len(member)==0:
        for i in range(N):
            dfs(member+[i])
    else:
        for i in range(member[-1]+1, N):
            dfs(member+[i])

dfs([])
print(min_dif)