# Digit Generator

N = int(input())
checkStart = N - (len(str(N)) * 9)
if checkStart <= 0:
    checkStart = 1

bunhaehap = 0
for i in range(checkStart, N):
    bunhaehap = 0
    for j in str(i):
        bunhaehap += int(j)
    bunhaehap += i
    if bunhaehap == N:
        print(i)
        break
if bunhaehap != N:
    print(0)
