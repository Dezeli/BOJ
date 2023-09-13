# 2007년

A, B = map(int, input().split(" "))
daysPerMonthDict = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}
date = 0
for i in range(1, A):
    date += daysPerMonthDict[i]
date += B
if date % 7 == 1:
    print("MON")
elif date % 7 == 2:
    print("TUE")
elif date % 7 == 3:
    print("WED")
elif date % 7 == 4:
    print("THU")
elif date % 7 == 5:
    print("FRI")
elif date % 7 == 6:
    print("SAT")
else:
    print("SUN")
    