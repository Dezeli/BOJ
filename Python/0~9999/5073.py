# 삼각형과 세 변

while True:
    a, b, c = map(int, input().split())

    if a == b == c == 0:
        break

    if max([a, b, c]) * 2 >= sum([a, b, c]):
        print("Invalid")
        continue

    if a == b == c:
        print("Equilateral")
    elif a == b or b == c or c == a:
        print("Isosceles")
    else:
        print("Scalene")
