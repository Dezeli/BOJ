# 쿠키애호가

T = int(input())

for _ in range(T):
    N, C = map(int, input().split())

    if N % C:
        print(N // C + 1)
    else:
        print(N // C)
