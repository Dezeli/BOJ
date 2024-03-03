# Basketball One-on-One

A = 0
B = 0

S = input()

score = ""
for i in S:
    if i == "A":
        score = "A"
    elif i == "B":
        score = "B"
    else:
        if score == "A":
            A += int(i)
        else:
            B += int(i)

if A > B:
    print("A")
else:
    print("B")
