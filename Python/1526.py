# 가장 큰 금민수
import sys

N = int(sys.stdin.readline().rstrip())

for i in range(N):
    num = N - i
    check = 0
    for j in str(num):
        if j == "7" or j == "4":
            pass
        else:
            check = 1
            break
    if check == 0:
        break
print(num)
