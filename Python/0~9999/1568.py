# 새
import sys

N = int(sys.stdin.readline().rstrip())

cnt = 0
song = 0
fly = 0
while True:
    cnt += 1
    song += 1
    if fly + song > N:
        song = 1
    fly += song

    if fly == N:
        break

print(cnt)
