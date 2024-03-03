# 직각삼각형

lines = list(map(int, input().split()))
while lines != [0, 0, 0]:
    lines.sort()
    if lines[0] ** 2 + lines[1] ** 2 == lines[2] ** 2:
        print("right")
    else:
        print("wrong")

    lines = list(map(int, input().split()))
