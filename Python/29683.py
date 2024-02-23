# Рождественская лотерея

n, A = map(int, input().split())
a = list(map(int, input().split()))

cnt = 0

for i in a:
    cnt += i//A
print(cnt)