# 팀 이름 정하기
import sys

boyName = sys.stdin.readline().rstrip()
N = int(sys.stdin.readline().rstrip())
score = 0
name = []
bl = boyName.count("L")
bo = boyName.count("O")
bv = boyName.count("V")
be = boyName.count("E")
for _ in range(N):
    girlNname = sys.stdin.readline().rstrip()
    l = girlNname.count("L") + bl
    o = girlNname.count("O") + bo
    v = girlNname.count("V") + bv
    e = girlNname.count("E") + be
    newScore = ((l + o) * (l + v) * (l + e) * (o + v) * (o + e) * (v + e)) % 100
    if score < newScore:
        score = newScore
        name = [girlNname]
    elif score == newScore:
        name.append(girlNname)
print(sorted(name)[0])
