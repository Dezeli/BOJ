# 꿍의 우주여행

T = int(input())

for _ in range(T):
    N, D = map(int, input().split())
    cnt = 0
    for __ in range(N):
        v, f, c = map(int, input().split())
        if v*f/c >= D:
            cnt += 1
    print(cnt)