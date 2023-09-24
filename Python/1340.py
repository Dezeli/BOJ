# 연도 진행바
import datetime
import sys

month, day, year, time = sys.stdin.readline().split(" ")
monthDict = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12,
}
year = int(year)
month = monthDict[month]
day = int(day[:-1])
H, M = map(int, time.split(":"))
start = datetime.datetime(year, 1, 1, 0, 0)
finish = datetime.datetime(year, month, day, H, M)
total = datetime.datetime(year + 1, 1, 1, 0, 0)
print((finish - start) / (total - start) * 100)
