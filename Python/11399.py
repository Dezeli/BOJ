# ATM
import sys

N = int(sys.stdin.readline().rstrip())

times = list(map(int, sys.stdin.readline().split(" ")))
times.sort(reverse=True)

every_time = 0
for i in range(1, N + 1):
    every_time += i * times[i - 1]

print(every_time)
