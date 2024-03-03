# Score

T = int(input())

for i in range(T):
    Q = input()
    correct = Q.split("X")
    correctSum = 0
    for j in correct:
        for k in range(len(j)):
            correctSum += k + 1
    print(correctSum)
