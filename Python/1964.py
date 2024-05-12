# 오각형, 오각형, 오각형…

N = int(input())
dots = 5
for i in range(2, N + 1):
    dots += 7 + (i - 2) * 3

print(dots % 45678)
