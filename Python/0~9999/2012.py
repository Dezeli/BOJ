# 등수 매기기
import sys

input = sys.stdin.readline

N = int(input())
predict = [int(input()) for _ in range(N)]
predict.sort()

cnt = 0
for i in range(1, N+1):
    cnt += abs(predict[i-1]-i)

print(cnt)