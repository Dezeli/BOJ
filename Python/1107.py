# 리모컨
from sys import stdin

N = int(stdin.readline().rstrip())
M = int(stdin.readline().rstrip())
if M:
    broken = list(stdin.readline().rstrip().split(" "))
else: 
    broken = []
if N==100:
    print(0)
elif N>100:
    min_press = N-100
    for i in range(N, 100, -1):
        press = True
        for j in str(i):
            if j in broken:
                press = False
                break
        if press==True:
            min_press = min([N-i+len(str(i)), min_press])
            break
    for i in range(N, 1000001):
        if min_press < i-N:
            break
        press = True
        for j in str(i):
            if j in broken:
                press = False
                break
        if press==True:
            min_press = min([i-N+len(str(i)), min_press])
            break
    print(min_press)
else:
    min_press = 100-N
    for i in range(N, -1, -1):
        press = True
        for j in str(i):
            if j in broken:
                press = False
                break
        if press==True:
            min_press = min([N-i+len(str(i)), min_press])
            break
    for i in range(N, 100):
        if min_press < i-N:
            break
        press = True
        for j in str(i):
            if j in broken:
                press = False
                break
        if press==True:
            min_press = min([i-N+len(str(i)), min_press])
            break
    print(min_press)