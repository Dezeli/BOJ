# 별 찍기 - 11
import sys
sys.setrecursionlimit(10**6)
N = int(input()) # N = 3 x 2^k
col = N*2-1

def star(num, line):
    global N
    next_line = [" " for _ in range(col+1)]
    print("".join(line[1:]))
    if num==N:
        return

    if num%3==1:
        for i in range(1, len(line)):
            if line[i]=="*":
                next_line[i-1] = "*"
                next_line[i+1] = "*"
    elif num%3==2:
        pair = True
        for i in range(1, len(line)):
            if line[i]=="*" and pair==True:
                for j in range(5):
                    next_line[i+j-1] = "*"
                pair = False
            elif line[i]=="*" and pair==False:
                pair = True
    elif num%3==0:
        for i in range(1, len(line)-1):
            if line[i-1]=="*" and line[i]==" " and line[i+1]==" ":
                next_line[i] = "*"
            if line[i-1]==" " and line[i]==" " and line[i+1]=="*":
                next_line[i] = "*"


    star(num+1, next_line)


line1 = [" " for _ in range(col+1)]
line1[col//2+1] = "*"
star(1, line1)
