# 2017 연세대학교 프로그래밍 경시대회

N = int(input())

cnt = 0
for n in range(1, N+1):
    for y in range(1, N-n):
        t = N-n-y
        if n<y+2:
            continue
        if t%2==1:
            continue
        cnt += 1
print(cnt)