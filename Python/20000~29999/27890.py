# 특별한 작은 분수

x, N = map(int, input().split())

for i in range(1, N + 1):
    if x % 2 == 0:
        x = (x // 2) ^ 6
    else:
        x = (x * 2) ^ 6

print(x)
