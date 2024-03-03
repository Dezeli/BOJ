# SPAVANAC

H, M = map(int, input().split(" "))
minute = H * 60 + M
minute -= 45
H = minute // 60
M = minute % 60
if minute < 0:
    H = 23
    M = 60 + minute
print(H, M)
