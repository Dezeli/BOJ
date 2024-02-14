# Electric Bill

o, a = map(int, input().split())
n = int(input())

for _ in range(n):
    e = int(input())
    if e>1000:
        print(e, o*1000 + a*(e-1000))
    else:
        print(e, e*o)