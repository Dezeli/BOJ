# 너의 평점은
import sys

input = sys.stdin.readline

grade = ["A+", "A0", "B+", "B0", "C+", "C0", "D+", "D0", "F"]
point = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0]

total = 0
result = 0
for _ in range(20):
    s, g, p = input().split()
    g = float(g)
    if p != "P":
        total += g
        result += g * point[grade.index(p)]

print("%.6f" % (result / total))
