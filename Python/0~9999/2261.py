# 가장 가까운 두 점
import sys
import math

input = sys.stdin.readline

n = int(input())
dots = [tuple(map(int, input().split())) for _ in range(n)]

dots.sort()

def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def min_dist(dots):
    if len(dots)==2:
        return dist(dots[0], dots[1])
    else:
        return min(dist(dots[0], dots[1]), dist(dots[1], dots[2]), dist(dots[2], dots[0]))

def join_strip(dots, min_val):
    mid = len(dots)//2
    strip_l = dots[mid][0]-min_val
    strip_r = dots[mid-1][0]+min_val
    
    strip = []
    for x, y in dots:
        if strip_l<x<strip_r:
            strip.append((x, y))

    strip.sort(key=lambda x: x[1])

    for i in range(len(strip)):
        for j in range(i+1, len(strip)):
            if (strip[j][1] - strip[i][1]) >= min_val:
                break
            min_val = min(min_val, dist(strip[i], strip[j]))
    return min_val


def search(dots):
    if len(dots)<=3:
        return min_dist(dots)
    
    mid = len(dots)//2
    left = search(dots[:mid])
    right = search(dots[mid:])

    return join_strip(dots, min(left, right))


print(round(search(dots)**2))