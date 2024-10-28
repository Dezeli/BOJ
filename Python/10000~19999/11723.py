# 집합
import sys
import collections

M = int(sys.stdin.readline().rstrip())
S = collections.defaultdict(int)

for _ in range(M):
    order = list(sys.stdin.readline().rstrip().split(" "))
    if order[0] == "add":
        S[order[1]] = 1
    elif order[0] == "remove":
        S[order[1]] = 0
    elif order[0] == "check":
        print(S[order[1]])
    elif order[0] == "toggle":
        if S[order[1]] == 1:
            S[order[1]] = 0
        else:
            S[order[1]] = 1
    elif order[0] == "all":
        S = collections.defaultdict(lambda: 1)
    elif order[0] == "empty":
        S = collections.defaultdict(int)
