# 토너먼트

N, kim, lim = map(int, input().split())

leag = [i for i in range(1, N + 1)]

cnt = 0
find = False
while True:
    cnt += 1
    win = len(leag) % 2
    for _ in range(len(leag) // 2):
        a = leag.pop(0)
        b = leag.pop(0)

        if (a == kim and b == lim) or (a == lim and b == kim):
            find = True
            break
        elif b == kim or b == lim:
            leag.append(b)
        else:
            leag.append(a)

    if win:
        leag.append(leag.pop(0))

    if find:
        break

print(cnt)
