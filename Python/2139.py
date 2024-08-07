# 나는 너가 살아온 날을 알고 있다
import datetime


while True:
    d, m, y = map(int, input().split())
    if d == 0 and m == 0 and y == 0:
        break
    input_d = datetime.datetime(year=y, month=m, day=d)
    std_d = datetime.datetime(year=y, month=1, day=1)

    info = input_d - std_d
    print(info.days + 1)
