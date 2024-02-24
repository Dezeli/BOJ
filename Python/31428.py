# 엘리스 트랙 매칭

N = int(input())

fTrack = list(input().split())
myTrack = input()
cnt = 0
for i in fTrack:
    if i==myTrack:
        cnt += 1

print(cnt)