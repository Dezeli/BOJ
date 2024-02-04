# Median

i = 0
while True:
    i += 1
    n = list(map(int, input().split()))
    if n[0]==0:
        break

    a = n[0]
    print(f"Case {i}: ", end="")
    if a%2==0:
        print("{:.1f}".format((n[a//2]+n[a//2+1])/2))
    else:
        print("{:.1f}".format(n[a//2+1]))