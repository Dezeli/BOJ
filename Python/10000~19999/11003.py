# 최솟값 찾기
import sys
from collections import deque

input = sys.stdin.readline

N, L = map(int, input().split())
A = list(map(int, input().split()))

dq = deque([])
ans = []


for i in range(L):
    if dq:
        while A[i] < dq[-1]:
            dq.pop()
            if not dq:
                break
    dq.append(A[i])
    ans.append(dq[0])


for i in range(L, N):
    if dq:
        while A[i] < dq[-1]:
            dq.pop()
            if not dq:
                break
    dq.append(A[i])

    if A[i - L] == dq[0]:
        dq.popleft()

    ans.append(dq[0])

print(*ans)
