# 공백 없는 A+B
import sys

S = sys.stdin.readline().rstrip()

if len(S) == 3:
    if int(S[1:3]) == 10:
        print(int(S[0]) + int(S[1:3]))
    else:
        print(int(S[0:2]) + int(S[2]))
elif len(S) == 4:
    print(20)
else:
    print(int(S[0]) + int(S[1]))
