# 미국 스타일

T = int(input())

for _ in range(T):
    n, s = input().split()

    if s == "kg":
        print("{:.4f} lb".format(float(n) * 2.2046))
    elif s == "lb":
        print("{:.4f} kg".format(float(n) * 0.4536))
    elif s == "l":
        print("{:.4f} g".format(float(n) * 0.2642))
    elif s == "g":
        print("{:.4f} l".format(float(n) * 3.7854))
