# solved.ac
import sys

n = int(sys.stdin.readline().rstrip())
opinions = []

for _ in range(n):
    opinion = int(sys.stdin.readline().rstrip())
    opinions.append(opinion)

opinions.sort()
minus = n*15/100
if minus-int(minus)>=0.5:
    minus = int(minus)+1
else:
    minus = int(minus)
julopinions = opinions[minus:n-minus]
if julopinions:
    avgop = sum(julopinions)/len(julopinions)
    if avgop-int(avgop)>=0.5:
        avgop = int(avgop)+1
    else:
        avgop = int(avgop)
    print(avgop)
else:
    print(0)