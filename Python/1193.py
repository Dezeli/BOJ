# 분수찾기

X = int(input())

X += 1
time = 0
H = 1
i = 0
while X > H:
    H += i
    i += 1
    time += 1

H -= i - 1
W = X - H
if time % 2 == 1:
    print(f"{W}/{time-W}")
else:
    print(f"{time-W}/{W}")
