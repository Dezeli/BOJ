# 24
import datetime
import sys

sH, sM, sS = map(int, sys.stdin.readline().split(":"))
nH, nM, nS = map(int, sys.stdin.readline().split(":"))


start_time = datetime.timedelta(hours=sH, minutes=sM, seconds=sS)
now_time = datetime.timedelta(hours=nH, minutes=nM, seconds=nS)

time_difference = str(now_time - start_time)
result_time = time_difference.split()[-1]
if len(result_time) == 7:
    print("0", end="")
print(result_time)
