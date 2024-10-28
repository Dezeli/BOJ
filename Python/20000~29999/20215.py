# Cutting Corners

w, h = map(int, input().split())
result = w + h - (w**2 + h**2) ** (1 / 2)
print(result)
