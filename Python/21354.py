# Äpplen och päron

A, P = map(int, input().split())

if A * 7 > P * 13:
    print("Axel")
elif A * 7 == P * 13:
    print("lika")
else:
    print("Petra")
