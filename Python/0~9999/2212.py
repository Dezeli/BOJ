# 센서
import sys

input = sys.stdin.readline

N = int(input())
K = int(input())

sensors = list(map(int, input().split()))
sensors.sort()

dis = []
last = sensors[0]
for i in sensors[1:]:
    dis.append(i - last)
    last = i

dis.sort()
print(sum(dis[: N - K]))
