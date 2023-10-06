# ACM Hotel 

T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())
    floor = N % H
    room_num = N // H + 1
    if floor == 0:
        floor = H
        room_num -= 1
    if room_num < 10:
        print(str(floor) + "0" + str(room_num))
    else:
        print(str(floor) + str(room_num) + " ")
