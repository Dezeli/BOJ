# 평균 점수

scoreList = []
for i in range(5):
    scoreList.append(int(input()))


def avg(scores):
    total = 0
    for singleScore in scores:
        if singleScore < 40:
            total += 40
        else:
            total += singleScore
    average = int(total / 5)
    return average


print(avg(scoreList))
