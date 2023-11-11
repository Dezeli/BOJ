# 숨바꼭질
import sys
from collections import deque


N, K = map(int, sys.stdin.readline().split(" "))

ran = 100

times = [0 for _ in range(ran+1)]

for i in range(ran+1):
    if i < N:
        times[i] = N-i
    elif i==N:
        times[i] = 0
    else:
        if i%2==0:
            times[i] = min(times[i-1]+1, times[i//2]+1)
        else:
            times[i] = times[i-1]+1

for i in range(ran-1, -1, -1):
    times[i] = min([times[i], times[i+1]+1])

for i in range(ran+1):
    if i%2==0:
        times[i] = min(times[i], times[i//2]+1)
    else:
        times[i] 

print(times[K])
for i in range(len(times)):
    print(f"{i}. {times[i]}")
