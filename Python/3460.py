# 이진수

T = int(input())

for _ in range(T):
    pos = []
    num = int(input())
    i = 0
    while True:
        if num == 0:
            break
        if num % 2 == 1:
            pos.append(i)
        num //= 2
        i += 1
    print(*pos)
