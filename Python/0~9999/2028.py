# 자기복제수

T = int(input())

for _ in range(T):
    N = int(input())
    N2 = str(N**2)[::-1][: len(str(N))][::-1]
    if str(N) == N2:
        print("YES")
    else:
        print("NO")
