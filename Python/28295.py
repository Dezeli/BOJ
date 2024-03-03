# 체육은 코딩과목 입니다


dir = 0
for _ in range(10):
    dir += int(input())

if dir % 4 == 0:
    print("N")
elif dir % 4 == 1:
    print("E")
elif dir % 4 == 2:
    print("S")
else:
    print("W")
