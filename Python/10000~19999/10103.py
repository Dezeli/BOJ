# 주사위 게임

n = int(input())

ap = 100
bp = 100
for _ in range(n):
    a, b = map(int, input().split())
    if a>b:
        bp -= a
    elif a<b:
        ap -= b
    
print(ap)
print(bp)