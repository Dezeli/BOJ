# 개표

A = 0
B = 0
V = int(input())
for i in input():
    if i == "A":
        A += 1
    else:
        B += 1
if A > B:
    print("A")
elif A == B:
    print("Tie")
else:
    print("B")
