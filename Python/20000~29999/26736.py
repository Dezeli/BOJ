# Wynik meczu

S = input()
A = 0
B = 0
for s in S:
    if s == "A":
        A += 1
    else:
        B += 1

print(f"{A} : {B}")
