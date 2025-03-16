# UCPC는 무엇의 약자일까?
import sys

input = sys.stdin.readline

s = input().rstrip()

c = ['U', 'C', 'P', 'C']
a = 0

for i in s:
    if i == c[a]:
        a += 1
        if a>3:
            print('I love UCPC')
            break

if a<=3:
    print('I hate UCPC')
