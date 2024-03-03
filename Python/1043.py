# 거짓말
import sys
from collections import defaultdict

input = sys.stdin.readline

N, M = map(int, input().split(" "))
Truth = list(map(int, input().split(" ")))
people = defaultdict(set)
parties = []
Truth_check = [0 for _ in range(N + 1)]

for _ in range(M):
    party = list(map(int, input().split(" ")))[1:]
    parties.append(party)
    for i in party:
        people[i].update(party)


while len(Truth) > 1:
    person = Truth.pop()
    if Truth_check[person]:
        continue
    else:
        Truth += people[person]
        Truth_check[person] = 1


lie = 0
for party in parties:
    say = True
    for i in party:
        if Truth_check[i]:
            say = False
            break
    if say:
        lie += 1

print(lie)
