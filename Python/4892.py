# 숫자 맞추기 게임


i = 0
while True:
    n = int(input())
    if n == 0:
        break
    i += 1

    n1 = n * 3

    if n1 % 2 == 0:
        n2 = n1 // 2
    else:
        n2 = (n1 + 1) // 2

    n3 = n2 * 3

    n4 = n3 // 9

    if n1 % 2 == 0:
        print(f"{i}. even {n4}")
    else:
        print(f"{i}. odd {n4}")
