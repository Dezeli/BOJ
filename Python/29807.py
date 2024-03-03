# 학번을 찾아줘!

T = int(input())

scores = list(map(int, input().split())) + [0 for _ in range(5)]
num = 0

K = scores[0]
E = scores[2]
M = scores[1]
S = scores[3]
F = scores[4]

if K > E:
    num += (K - E) * 508
else:
    num += (E - K) * 108

if M > S:
    num += (M - S) * 212
else:
    num += (S - M) * 305

num += F * 707

print(num * 4763)
