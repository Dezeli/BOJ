# Basketball Score

a1, a2, a3 = map(int, input().split())
b1, b2, b3 = map(int, input().split())

a = a1+a2*2+a3*3
b = b1+b2*2+b3*3

if a>b:
    print(1)
elif a==b:
    print(0)
else:
    print(2)