# 세탁소 사장 동혁

T = int(input())

for _ in range(T):
    left = int(input())
    Q = left//25
    left -= Q*25
    D = left//10
    left -= D*10
    N = left//5
    left -= N*5
    P = left

    print(Q, D, N, P)