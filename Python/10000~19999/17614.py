# 369
import sys

input = sys.stdin.readline

N = int(input())

clap = 0
for i in range(1, N + 1):
    while i > 0:
        i, left = divmod(i, 10)
        if left == 3 or left == 6 or left == 9:
            clap += 1
print(clap)
