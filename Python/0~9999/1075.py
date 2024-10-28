# 나누기
import sys

N = sys.stdin.readline().rstrip()
F = int(sys.stdin.readline().rstrip())
new_N = N[:-2]
for i in range(0, 100):
    i = str(i)
    if len(i) == 1:
        i = "0" + i
    if int(new_N + i) % F == 0:
        print(i)
        break
