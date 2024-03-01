# 나는 요리사다

max_score = 0
num = 0
for i in range(1, 6):
    scores = list(map(int, input().split()))

    if sum(scores) > max_score:
        num = i
        max_score = sum(scores)

print(num, max_score)