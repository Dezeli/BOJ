# 문자열 압축 해제
import sys

input = sys.stdin.readline

N = int(input())

pattern = {}

for _ in range(N):
    L, U = input().rstrip().split()
    pattern[U] = L

Ustr = input().rstrip()
Lstr = ''
for s in Ustr:
    Lstr += pattern[s]


S, E = map(int, input().split())
print(Lstr[S-1:E])