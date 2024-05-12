# 국영수
import sys

input = sys.stdin.readline

N = int(input())

student = []

for i in range(N):
    n, k, e, m = input().rstrip().split()
    k = -int(k)
    e = int(e)
    m = -int(m)
    student.append([k, e, m, n])

student.sort()

for i in student:
    print(i[3])
