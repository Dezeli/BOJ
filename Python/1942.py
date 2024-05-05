# 디지털 시계
import datetime
from datetime import timedelta
 
for i in range(3):
    s, e = input().split()
 
    st = int(s.replace(":", ""))
    ed = int(e.replace(":", ""))
 
    stH, stM, stS = map(int, s.split(":"))
    edH, edM, edS = map(int, e.split(":"))
 
    stime = datetime.datetime(2024, 1, 1, stH, stM, stS)
    tmp_time = stime.strftime('%H%M%S')
 
    sec=1
    cnt=0
    if int(tmp_time)%3==0:
        cnt += 1
    etime = datetime.datetime(2024, 1, 1, edH, edM, edS)
    etime = etime.strftime('%H%M%S')
 
    while True:
        if tmp_time==etime:
            break
        
        stime = stime+timedelta(seconds=sec)
        tmp_time = stime.strftime('%H%M%S')
        if int(tmp_time)%3==0:
            cnt+=1
 
    print(cnt)