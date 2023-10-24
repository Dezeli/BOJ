# 열 개씩 끊어 출력하기

N = input()

time = (len(N) + 1) // 10
for i in range(len(N)):
    print(N[i], end="")
    if (i + 1) % 10 == 0:
        print()
