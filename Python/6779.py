# Who Has Seen The Wind

h = int(input())
M = int(input())

g = False
for t in range(1, M+1):
    A = -6*(t**4) + h*(t**3) + 2*(t**2) + t
    if A <= 0:
        g = True
        break

if g:
    print(f"The balloon first touches ground at hour: {t}")
else:
    print(f"The balloon does not touch ground in the given time.")