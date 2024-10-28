# 사탕 선생 고창영

T = int(input())

for _ in range(T):
    input()
    N = int(input())
    candy = 0
    for __ in range(N):
        candy += int(input())

    if candy % N == 0:
        print("YES")
    else:
        print("NO")
