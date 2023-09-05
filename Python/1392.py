# Music Notes
import sys

N, Q = map(int, sys.stdin.readline().split())

scores = [0]
for i in range(N):
    score = int(sys.stdin.readline().rstrip()) + scores[-1]
    scores.append(score)
scores.pop(0)

for i in range(Q):
    question = int(sys.stdin.readline().rstrip())
    for j in range(len(scores)):
        if scores[j] > question:
            print(j + 1)
            break
