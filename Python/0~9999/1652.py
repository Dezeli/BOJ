# 누울 자리를 찾아라
import sys

N = int(sys.stdin.readline().rstrip())
wseat = 0
hseat = 0
height = ["" for i in range(N)]

for _ in range(N):
    line = sys.stdin.readline().rstrip()
    for i in range(N):
        height[i] += line[i]
    seat = line.split("X")
    for i in range(2, N + 1):
        wseat += seat.count("." * i)

for line in height:
    line = "".join(line)
    seat = line.split("X")
    for i in range(2, N + 1):
        hseat += seat.count("." * i)

print(wseat, hseat)
