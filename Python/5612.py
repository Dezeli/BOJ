# 터널의 입구와 출구

n = int(input())
car = [int(input())]

for i in range(n):
    t, c = map(int, input().split())
    car.append(car[i] + t - c)

check = True
for i in range(n + 1):
    if car[i] < 0:
        print(0)
        check = False
        break
if check:
    print(max(car))
