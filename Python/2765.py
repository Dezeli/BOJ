# 자전거 속도
import math

num = 0
while True:
    num += 1
    d, r, t = map(float, input().split())
    if r == 0:
        break
    dis = d / 63360 * math.pi * r
    mph = dis / t * 3600
    print("Trip #%d: %.2f %.2f" % (num, dis, mph))
