# 상금 헌터

T = int(input())

p1 = [0, 500, 300, 300, 200, 200, 200, 50, 50, 50, 50, 30, 30, 30, 30, 30, 10, 10, 10, 10, 10, 10]
p2 = [0, 512]+[256]*2+[128]*4+[64]*8+[32]*16

for _ in range(T):
    a, b = map(int, input().split())

    p = 0
    if a<=21:
        p += p1[a]
    if b<=31:
        p += p2[b]
    
    print(p*10000)