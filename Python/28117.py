# prlong longf
import sys

input = sys.stdin.readline

N = int(input())
S = list(input().rstrip().split("long"))
if len(S) > 1:
    S.pop(0)
    S.pop()

cases = [1, 2]
for _ in range(20):
    cases.append(cases[-1] + cases[-2])

cnt = 0
c = 1
for i in S:
    if i == "":
        cnt += 1
    else:
        c *= cases[cnt]
        cnt = 0
c *= cases[cnt]
print(c)
