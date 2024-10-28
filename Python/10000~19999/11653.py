# 소인수분해

N = int(input())

while N != 1:
    num = 1
    while True:
        num += 1
        if N % num == 0:
            print(num)
            N = N // num
            break
