# 롤 케이크
import sys

input = sys.stdin.readline

L = int(input())
N = int(input())

cake = [1 for i in range(L+1)]
score = [-1]
expect = [-1]
for _ in range(N):
    s = 0
    P, K = map(int, input().split())
    expect.append(K-P+1)
    for i in range(P, K+1):
        if cake[i]:
            cake[i] = 0
            s += 1
    score.append(s)

    
print(expect.index(max(expect)))
print(score.index(max(score)))