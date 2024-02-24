# 준영이의 등급

N, K = map(int, input().split())

G = list(map(int, input().split()))
score = []

for i in G:
    per = i*100//N
    if per<=4:
        score.append(1)
    elif per<=11:
        score.append(2)
    elif per<=23:
        score.append(3)
    elif per<=40:
        score.append(4)
    elif per<=60:
        score.append(5)
    elif per<=77:
        score.append(6)
    elif per<=89:
        score.append(7)
    elif per<=96:
        score.append(8)
    else:
        score.append(9)

print(*score)