# Above Average

C = int(input())

for i in range(C):
    studentArrayScore = input().split(" ")
    for j in range(len(studentArrayScore)):
        studentArrayScore[j] = int(studentArrayScore[j])
    up = 0
    avg = (sum(studentArrayScore) - studentArrayScore[0]) / studentArrayScore[0]
    for j in range(1, len(studentArrayScore)):
        if studentArrayScore[j] > avg:
            up += 1
    result = up / studentArrayScore[0] * 100
    print("%0.3f" % result, end="")
    print("%")
