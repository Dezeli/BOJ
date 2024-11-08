# Короли

n, m, k, a, b, c = map(int, input().split())

max_sol = max(n * a, m * b, k * c)
king = []
if n * a == max_sol:
    king.append("Joffrey")
if m * b == max_sol:
    king.append("Robb")
if k * c == max_sol:
    king.append("Stannis")

print(*king)
