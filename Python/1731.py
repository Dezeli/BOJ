# 추론
import sys

T = int(sys.stdin.readline().rstrip())

num_list = []

for _ in range(T):
    num_list.append(int(sys.stdin.readline().rstrip()))

if num_list[1] - num_list[0] == num_list[2] - num_list[1]:
    print(num_list[-1] + (num_list[1] - num_list[0]))
else:
    print(int(num_list[-1] * (num_list[1] / num_list[0])))
