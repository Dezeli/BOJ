# 암호키
import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    num = int(sys.stdin.readline().rstrip())
    i = 2
    result = True
    while i <= 10**6:
        if num % i == 0:
            result = False
            break
        i += 1

    if result == True:
        print("YES")
    else:
        print("NO")
