# 멍멍이 쓰다듬기

X, Y = map(int, input().split())

if X==Y:
    print(0)

else:
    grow = 0
    i = 1
    while grow<Y-X:
        grow += i*2
        i += 1
    i -= 1
    if grow - i >=Y-X:
        print(i*2-1)
    else:
        print(i*2)