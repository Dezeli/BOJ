# 빵

N = int(input())

min_time = 2e9

for _ in range(N):
    A, B = map(int, input().split())

    if A<=B:
        min_time = min(min_time, B)

if min_time != 2e9:
    print(min_time)
else:
    print(-1)
