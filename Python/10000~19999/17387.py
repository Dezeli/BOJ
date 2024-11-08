# 선분 교차 2
import sys

input = sys.stdin.readline


def solution():
    ccw123 = ccw(x1, y1, x2, y2, x3, y3)
    ccw124 = ccw(x1, y1, x2, y2, x4, y4)
    ccw341 = ccw(x3, y3, x4, y4, x1, y1)
    ccw342 = ccw(x3, y3, x4, y4, x2, y2)

    if ccw123 * ccw124 == 0 and ccw341 * ccw342 == 0:
        if min_x <= max_x and min_y <= max_y:
            return 1
    elif ccw123 * ccw124 <= 0 and ccw341 * ccw342 <= 0:
        return 1
    return 0


def ccw(x1, y1, x2, y2, x3, y3):
    return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)


if __name__ == "__main__":
    x1, y1, x2, y2 = list(map(int, input().split()))
    x3, y3, x4, y4 = list(map(int, input().split()))

    min_x = max(min(x1, x2), min(x3, x4))
    min_y = max(min(y1, y2), min(y3, y4))
    max_x = min(max(x1, x2), max(x3, x4))
    max_y = min(max(y1, y2), max(y3, y4))

    print(solution())
