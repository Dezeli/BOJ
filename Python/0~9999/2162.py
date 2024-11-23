# 선분 그룹
import sys

input = sys.stdin.readline


def ccw(x1, y1, x2, y2, x3, y3):
    return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)


def isCross(x1, y1, x2, y2, x3, y3, x4, y4):
    ccw123 = ccw(x1, y1, x2, y2, x3, y3)
    ccw124 = ccw(x1, y1, x2, y2, x4, y4)
    ccw341 = ccw(x3, y3, x4, y4, x1, y1)
    ccw342 = ccw(x3, y3, x4, y4, x2, y2)

    min_x = max(min(x1, x2), min(x3, x4))
    min_y = max(min(y1, y2), min(y3, y4))
    max_x = min(max(x1, x2), max(x3, x4))
    max_y = min(max(y1, y2), max(y3, y4))

    if ccw123 * ccw124 == 0 and ccw341 * ccw342 == 0:
        if min_x <= max_x and min_y <= max_y:
            return 1
    elif ccw123 * ccw124 <= 0 and ccw341 * ccw342 <= 0:
        return 1
    return 0


N = int(input())
group = [0 for _ in range(N)]
lines = []
next_group = 1

lines = []
for i in range(N):
    num = next_group
    l = list(map(int, input().split()))
    same = [0 for _ in range(next_group + 1)]
    for j in range(i):
        if isCross(*(l + lines[j])):
            num = min(num, group[j])
            same[group[j]] = 1

    for j in range(i):
        if same[group[j]] == 1:
            group[j] = num

    group[i] = num
    lines.append(l)

    if num == next_group:
        next_group += 1

set_group = set(group)
print(len(set_group))
max_cnt = 0
for i in set_group:
    max_cnt = max(max_cnt, group.count(i))

print(max_cnt)
