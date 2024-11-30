# 지영 공주님의 마법 거울

N = int(input())

mirror = [input() for _ in range(N)]

K = int(input())

if K==1:
    for l in mirror:
        print(l)
elif K==2:
    for l in mirror:
        print(l[::-1])
else:
    for l in mirror[::-1]:
        print(l)
