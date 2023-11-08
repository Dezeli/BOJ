# 잃어버린 괄호
import sys

cal = sys.stdin.readline().rstrip()

cal_list = list(cal.split("-"))
plus_list = list(cal_list[0].split("+"))
minus_list = []
for val in cal_list[1:]:
    minus_list += list(val.split("+"))

cal_val = 0
for i in plus_list:
    cal_val += int(i)
for i in minus_list:
    cal_val -= int(i)

print(cal_val)