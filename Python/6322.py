# 직각 삼각형의 두 변

i = 1
while True:
    a, b, c = map(int, input().split())

    if a==b==c==0:
        break
    if i>1:
        print()
    print(f"Triangle #{i}")

    if c==-1:
        print("c = %.3f" % ((a**2+b**2)**0.5))
    elif max(a, b) >= c:
        print("Impossible.")
    elif a==-1:
        print("a = %.3f" % ((c**2-b**2)**0.5))
    elif b==-1:
        print("b = %.3f" % ((c**2-a**2)**0.5))    
    i += 1