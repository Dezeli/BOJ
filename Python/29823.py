# Pakirobot Manhattanis

N = int(input())

S = input()

ns, we = 0, 0
for i in S:
    if i == 'N': ns += 1
    elif i == 'S': ns -= 1
    elif i == 'W': we += 1
    else: we -= 1
print(abs(ns)+abs(we))