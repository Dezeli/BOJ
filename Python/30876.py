# Tren del Fin del Mundo

N = int(input())

dots = []

for _ in range(N):
    x, y = map(int, input().split())
    dots.append([y, x])

print(*(min(dots)[::-1]))
