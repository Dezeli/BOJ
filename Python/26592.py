# Triangle Height

n = int(input())

for _ in range(n):
    area, base = map(float, input().split())
    h = area*2/base

    print("The height of the triangle is {:.2f} units".format(h))