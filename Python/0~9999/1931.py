# 회의실 배정
import sys

N = int(sys.stdin.readline().rstrip())

meetings = []

for _ in range(N):
    start, end = map(int, sys.stdin.readline().split(" "))
    meetings.append((start, end))

meetings.sort(key=lambda x: (x[1], x[0]))

meet_cnt = 0
meet_end = 0
for start, end in meetings:
    if start >= meet_end:
        meet_cnt += 1
        meet_end = end
print(meet_cnt)
