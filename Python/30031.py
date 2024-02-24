# 지폐 세기

N = int(input())

money = 0

for _ in range(N):
    w, h = map(int, input().split())
    if w==136:
        money += 1000
    elif w==142:
        money += 5000
    elif w==148:
        money += 10000
    else:
        money += 50000
print(money)

