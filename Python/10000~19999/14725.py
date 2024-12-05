# 개미굴
import sys

input = sys.stdin.readline

N = int(input())

datas = [list(input().rstrip().split())[1:] for _ in range(N)]
datas.sort()

last_data = [0]
for d in datas:
    for i in range(len(d)):
        if last_data[i] != d[i]:
            break
    for j in range(i, len(d)):
        print("--" * j + d[j])
    last_data = d
