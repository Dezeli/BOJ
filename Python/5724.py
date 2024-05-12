# 파인만

while True:
    N = int(input())
    if N == 0:
        break
    cnt = 0
    for i in range(1, N + 1):
        cnt += (N - i + 1) ** 2
    print(cnt)
