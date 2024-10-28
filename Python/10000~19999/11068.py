# 회문인 수
import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    ans = []
    for i in range(2, 65):
        li = []
        temp = n
        while temp != 0:
            li.append(temp % i)
            temp = temp // i
        for k in range(len(li) // 2):
            if li[k] != li[-1 - k]:
                ans.append("X")
                break
    if len(ans) == 63:
        print(0)
    else:
        print(1)
