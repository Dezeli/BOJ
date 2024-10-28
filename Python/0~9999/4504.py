# 배수 찾기

n = int(input())

while True:
    a = int(input())
    if a == 0:
        break

    if a % n == 0:
        print(f"{a} is a multiple of {n}.")
    else:
        print(f"{a} is NOT a multiple of {n}.")
