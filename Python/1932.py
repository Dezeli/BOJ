# 정수 삼각형
import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())

triangle = deque()
for _ in range(n):
    floor = [0] + list(map(int, sys.stdin.readline().split(" "))) + [0]
    triangle.append(floor)


while triangle:
    floor = triangle.popleft()

    if triangle:
        for i in range(1, len(floor)):
            triangle[0][i] += max([floor[i-1], floor[i]])
    
print(max(floor))