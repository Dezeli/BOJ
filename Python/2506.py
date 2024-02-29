# 점수계산

N = int(input())
scores = list(map(int, input().split()))

sum_score = 0
cnt = 0
for i in scores:
    if i==1:
        cnt += 1
        sum_score += cnt
    else:
        cnt = 0

print(sum_score)