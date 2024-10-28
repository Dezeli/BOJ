# 평행사변형
import sys

input = sys.stdin.readline


Xa, Ya, Xb, Yb, Xc, Yc = map(int, input().split())


def cal():
    line = [
        ((Xa - Xb) ** 2 + (Ya - Yb) ** 2) ** (1 / 2),
        ((Xb - Xc) ** 2 + (Yb - Yc) ** 2) ** (1 / 2),
        ((Xc - Xa) ** 2 + (Yc - Ya) ** 2) ** (1 / 2),
    ]
    print((max(line) - min(line)) * 2)


if Ya - Yb == 0 or Yb - Yc == 0:
    if Ya - Yb == 0 and Yb - Yc == 0:
        print(-1)
    else:
        cal()
elif Xa - Xb == 0 or Xb - Xc == 0:
    if Xa - Xb == 0 and Xb - Xc == 0:
        print(-1)
    else:
        cal()
elif (Xa - Xb) / (Ya - Yb) == (Xb - Xc) / (Yb - Yc):
    print(-1)
else:
    cal()
