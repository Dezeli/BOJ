# 평범한 배낭
import sys

input = sys.stdin.readline

N, K = map(int, input().split(" "))

bag = [0 for _ in range(K+1)]

for _ in range(N):
    W, V = map(int, input().split(" "))
    for i in range(W, K+1):
        bag[i-W] = max([bag[i] + V, bag[i-W]])

print(max(bag))