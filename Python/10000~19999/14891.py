# 톱니바퀴
import sys

input = sys.stdin.readline
W = [[i for i in input().rstrip()] for _ in range(4)]

idx = [6, 2, 6, 2, 6, 2, 6, 2]
rotate = [0]*4

K = int(input())
order = [list(map(int, input().split())) for _ in range(K)]


def move(s):
    ls = [s]

    for i in range(s, 0, -1):
        if W[i][idx[i*2]%8] == W[i-1][idx[i*2-1]%8]:
            break
        else:
            ls.append(i-1)

    for i in range(s, 3):
        if W[i][idx[i*2+1]%8] == W[i+1][idx[i*2+2]%8]:
            break
        else:
            ls.append(i+1)

    for i in ls:
        idx[i*2] += rotate[i]
        idx[i*2+1] += rotate[i]


for v1, v2 in order:
    v1 -= 1
    for i in range(4):
        if v1%2==i%2:
            rotate[i] = -v2
        else:
            rotate[i] = v2
    move(v1)

score = [int(W[i][(idx[i*2]+2)%8])*(2**i) for i in range(4)]
print(sum(score))