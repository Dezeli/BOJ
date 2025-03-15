# 통나무 건너뛰기
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    new_L1 = []
    new_L2 = []
    for i in range(0, N, 2):
        new_L1.append(L[i])
    for i in range(1, N, 2):
        new_L2.append(L[i])
    new_L2.reverse()
    new_L = new_L1 + new_L2
    
    max_d = abs(new_L[0]-new_L[-1])
    for i in range(N-1):
        max_d = max(max_d, abs(new_L[i]-new_L[i+1]))
    print(max_d)