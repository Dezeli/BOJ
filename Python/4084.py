# Viva la Diferencia

while True:
    a, b, c, d = map(int, input().split())
    if a==0 and b==0 and c==0 and d==0:
        break
    cnt = 0
    while not (a == b == c == d):
        a, b, c, d = abs(a-b), abs(b-c), abs(c-d), abs(d-a)
        cnt += 1
    print(cnt)