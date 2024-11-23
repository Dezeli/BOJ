# 장기


cho = 0
han = 1.5

a = list(map(int, input().split()))
b = list(map(int, input().split()))
score = [13, 7, 5, 3, 3, 2]

for i in range(6):
    cho += a[i] * score[i]
    han += b[i] * score[i]

if cho < han:
    print("ekwoo")
else:
    print("cocjr0208")
