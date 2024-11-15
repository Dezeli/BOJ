# 사과

N = int(input())

cnt = 0
for _ in range(N):
    a, b = map(int, input().split())
    cnt += b%a

print(cnt)