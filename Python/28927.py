# Киноманы

t1, e1, f1 = map(int, input().split())
t2, e2, f2 = map(int, input().split())

Max = t1*3 + e1*20 + f1*120
Mel = t2*3 + e2*20 + f2*120

if Max>Mel:
    print("Max")
elif Max==Mel:
    print("Draw")
else:
    print("Mel")