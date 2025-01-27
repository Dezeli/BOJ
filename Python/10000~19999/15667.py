# 2018 연세대학교 프로그래밍 경진대회

N = int(input())

i = 0
while True:
    i += 1
    if 1 + i + i**2 == N:
        print(i)
        break
