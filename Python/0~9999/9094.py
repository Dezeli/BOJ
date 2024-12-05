# 수학적 호기심

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    cnt = 0
    for a in range(1, n):
        for b in range(a + 1, n):
            if (a**2 + b**2 + m) % (a * b) == 0:
                cnt += 1
    print(cnt)
