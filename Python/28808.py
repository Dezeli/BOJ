# Таблица результатов

n, m = map(int, input().split())

cnt = 0
for _ in range(n):
    s = input()
    for i in s:
        if i=='+':
            cnt += 1
            break
print(cnt)