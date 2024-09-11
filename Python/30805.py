# 사전 순 최대 공통 부분 수열
import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

def sol(A, B, res):

    if (not A) or (not B):
        return res
    

    tmpA, tmpB = max(A), max(B)
    idxA, idxB = A.index(tmpA), B.index(tmpB)

    if tmpA == tmpB:
        res.append(tmpA)
        return sol(A[idxA + 1:], B[idxB + 1:], res)
    elif tmpA > tmpB:
        A.pop(idxA)
        return sol(A, B, res)
    else:
        B.pop(idxB)
        return sol(A, B, res)


ans = sol(A, B, [])

print(len(ans))
if ans:
    print(*ans)