# 양파 실험

N, A, B = map(int, input().split())

o1 = 1
o2 = 1

change = 1
for _ in range(N):
    if change == -1:
        o1 += B
        o2 += A
        if o2 < o1:
            change *= -1

    else:
        o1 += A
        o2 += B
        if o1 < o2:
            change *= -1
    if o1 == o2:
        if change == 1:
            o2 -= 1
        else:
            o1 -= 1


if change == 1:
    print(o1, o2)
else:
    print(o2, o1)
