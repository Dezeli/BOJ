# 영식이와 친구들
import sys

N, M, L = map(int, sys.stdin.readline().split())

friends = [0 for i in range(N)]
ball = 0
time = 0
friends[ball] += 1

while True:
    if M == 1:
        break
    time += 1
    if friends[ball] % 2 == 0:
        ball -= L
        if ball < 0:
            ball += N
        friends[ball] += 1
        if friends[ball] == M:
            break
    else:
        ball += L
        if ball >= N:
            ball -= N
        friends[ball] += 1
        if friends[ball] == M:
            break

print(time)
