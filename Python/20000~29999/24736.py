# Football Scoring

home = list(map(int, input().split()))
away = list(map(int, input().split()))

hscore = home[0] * 6 + home[1] * 3 + home[2] * 2 + home[3] * 1 + home[4] * 2
ascore = away[0] * 6 + away[1] * 3 + away[2] * 2 + away[3] * 1 + away[4] * 2
print(hscore, ascore)
