# Hot Dogs

while True:
    try:
        H, P = map(int, input().split())
        print("{:.2f}".format(round(H / P, 2)))
    except:
        break
