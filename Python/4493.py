# 가위 바위 보?

t = int(input())

for _ in range(t):
    n = int(input())
    score = 0
    for __ in range(n):
        p1, p2 = input().split()
        if p1 == "R" and p2 == "S":
            score += 1
        if p1 == "S" and p2 == "P":
            score += 1
        if p1 == "P" and p2 == "R":
            score += 1
        if p1 == "R" and p2 == "P":
            score -= 1
        if p1 == "S" and p2 == "R":
            score -= 1
        if p1 == "P" and p2 == "S":
            score -= 1
    if score > 0:
        print("Player 1")
    elif score == 0:
        print("TIE")
    else:
        print("Player 2")
