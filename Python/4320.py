# 완전 P제곱수
import sys

input = sys.stdin.readline


while True:
    x = int(input())
    if x==0:
        break
    
    if abs(x)==x:
        for i in range(31, 0, -1):
            if round(x**(1/i), 11)==int(round(x**(1/i), 11)):
                print(i)
                break
    else:
        for i in range(31, 0, -2):
            if round(abs(x)**(1/i), 11)==int(round(abs(x)**(1/i), 11)):
                print(i)
                break
