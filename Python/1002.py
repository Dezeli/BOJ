# 터렛

T = int(input())

for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split(" "))
    mid = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2)
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print("-1")
            continue
        else:
            print("0")
            continue
    if r1 > r2:
        if r1 - r2 > mid:
            print("0")
            continue
        elif r1 - r2 == mid:
            print("1")
            continue
    else:
        if r2 - r1 > mid:
            print("0")
            continue
        elif r2 - r1 == mid:
            print("1")
            continue
    if r1 + r2 < mid:
        print("0")
    elif r1 + r2 == mid:
        print("1")
    else:
        print("2")
