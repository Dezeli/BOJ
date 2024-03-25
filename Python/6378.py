# 디지털 루트

while True:
    n = int(input())
    if n==0:
        break
    while True:
        d_num = 0
        for i in str(n):
            d_num += int(i)
        n = d_num
        if d_num < 10:
            break
    print(d_num)
