# Pokemon Buddy

T = int(input())

for _ in range(T):
    G, C, E = map(int, input().split())

    if G==1:
        km = 1
    elif G==2:
        km = 3
    elif G==3:
        km = 5
    if C>E:
        print(0)
    else:
        print((E-C)*km)