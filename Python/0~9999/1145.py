# 적어도 대부분의 배수
import sys

num_List = list(map(int, sys.stdin.readline().split()))
num = min(num_List)
while True:
    div = 0
    for i in range(5):
        if num % num_List[i] == 0:
            div += 1
    if div > 2:
        print(num)
        break
    num += 1
