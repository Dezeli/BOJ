# 소수 부르기 게임
import sys

input = sys.stdin.readline

def isPrime(m, n):
    result = set()
    n += 1
    prime = [0] * n
    for i in range(2, int(n ** (1 / 2)) + 1):
        if prime[i] == 0:
            for j in range(2 * i, n, i):
                prime[j] = 1
    for i in range(m, n):
        if i > 1 and prime[i] == 0:
            result.add(i)
    return result

A, B = map(int, input().split())
C, D = map(int, input().split())


yt = isPrime(A, B)
yj = isPrime(C, D)
total = yt.union(yj)
both = len(yt) + len(yj) - len(total)

len_yt = len(yt)
len_yj = len(yj)
if both%2==1:
    len_yt += 1

if len_yt>len_yj:
    print("yt")
else:
    print("yj")    