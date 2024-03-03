# Speed Limit

while True:
    n = int(input())
    if n == -1:
        break
    dis = 0
    lastT = 0
    for __ in range(n):
        s, t = map(int, input().split())
        dis += s * (t - lastT)
        lastT = t

    print(dis, "miles")
