# NBA 농구
import sys

input = sys.stdin.readline

N = int(input())

prev =[0, 0]
team1 = [0, 0]
team2 = [0, 0]

for _ in range(N):
    win, time = input().rstrip().split()
    
    if win == '1':
        team1[0] += 1
    else:
        team2[0] += 1
    
    minute, second = map(int, time.split(":"))
    time = minute*60 + second
    
    if team1[0] == team2[0]:
        if prev[1] == 1:
            team1[1] += time - prev[0]
        else:
            team2[1] += time - prev[0]
        prev[1] = 0
    elif team1[0] > team2[0]:
        if prev[1] == 0:
            prev[0] = time
            prev[1] = 1
    else:
        if prev[1] == 0:
            prev[0] = time
            prev[1] = 2

if prev[1] == 1:
    team1[1] += 48*60 - prev[0]
if prev[1] == 2:
    team2[1] += 48*60 - prev[0]

print("%02d:%02d" %(team1[1]//60, team1[1]%60))
print("%02d:%02d" %(team2[1]//60, team2[1]%60))