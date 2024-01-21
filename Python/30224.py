# Lucky 7

N = input()

if int(N)%7!=0 and "7" not in N:
    print(0)
elif int(N)%7==0 and "7" not in N:
    print(1)
elif int(N)%7!=0 and "7" in N:
    print(2)
else:
    print(3)