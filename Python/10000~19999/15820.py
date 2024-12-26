# 맞았는데 왜 틀리죠?
import sys

input = sys.stdin.readline

S1, S2 = map(int, input().split())

for _ in range(S1):
    a, b = map(int, input().split())
    if a==b:
        S1 -= 1
for _ in range(S2):
    a, b = map(int, input().split())
    if a==b:
        S2 -= 1

if S1==0:
    if S2==0:
        print("Accepted")
    else:
        print("Why Wrong!!!")
else:
    print("Wrong Answer")