# Cornhole 

H1, B1 = map(int, input().split())
H2, B2 = map(int, input().split())
score1 = 3 * H1 + B1
score2 = 3 * H2 + B2

if score1>score2:
    print(1, score1-score2)
elif score1<score2:
    print(2, score2-score1)
else:
    print("NO SCORE")