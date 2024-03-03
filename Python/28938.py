# Конвейер

n = int(input())
moves = sum(list(map(int, input().split())))

if moves >= 1:
    print("Right")
elif moves == 0:
    print("Stay")
else:
    print("Left")
