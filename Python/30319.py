# Advance to Taoyuan Regional

Y, M, D = map(int, input().split('-'))

if M<9:
    print("GOOD")
elif M==9:
    if D<=16:
        print("GOOD")
    else:
        print("TOO LATE")
else:
    print("TOO LATE")