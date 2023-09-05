# 타임머신
import sys

times = list(map(int, sys.stdin.readline().split(":")))
times_list = []
for i in range(3):
    for j in range(2):
        make_time = list(times)
        new_times = [make_time.pop(i)]
        new_times.append(make_time.pop(j))
        new_times.append(make_time.pop(0))
        times_list.append(new_times)

cnt = 0
for i, j, h in times_list:
    if 1 <= i <= 12 and 0 <= j <= 59 and 0 <= h <= 59:
        cnt += 1

print(cnt)
