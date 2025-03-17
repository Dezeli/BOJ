# 파일 합치기 3
import sys
import heapq

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    K = int(input())
    files = list(map(int, input().split()))
    heapq.heapify(files)

    cnt = 0
    while len(files)>1:
        a = heapq.heappop(files)
        b = heapq.heappop(files)

        cnt += a + b
        heapq.heappush(files, a+b)
    
    print(cnt)