# 제곱 ㄴㄴ 수
import sys

minNum, maxNum = map(int, sys.stdin.readline().split())

squared_prime_list = [True] * (maxNum - minNum + 1)
for i in range(2, int(maxNum ** (1 / 2)) + 1):
    skip = minNum // (i**2)
    if (i**2) * skip - minNum < 0:
        skip += 1
    for i in range((i**2) * skip - minNum, len(squared_prime_list), i**2):
        squared_prime_list[i] = False

cnt = 0
for i in squared_prime_list:
    if i:
        cnt += 1
print(cnt)
