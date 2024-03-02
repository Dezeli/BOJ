# Transactions 

while True:
    a, b, c = input().split()

    if a=='0' and b=='W' and c=='0':
        break

    a = int(a)
    c = int(c)
    if b=='W':
        if a-c<-200:
            print("Not allowed")
        else:
            print(a-c)
    else:
        print(a+c)