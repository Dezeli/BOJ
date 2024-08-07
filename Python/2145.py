# 숫자 놀이

N = int(input())

while N != 0:
    while N > 9:
        N = sum([int(i) for i in str(N)])
    print(N)
    N = int(input())
