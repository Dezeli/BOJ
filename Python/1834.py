# 나머지와 몫이 같은 수
import sys

N = int(sys.stdin.readline().rstrip())

sum_num = 0

for i in range(1, N):
    sum_num += N * i + i

print(sum_num)
