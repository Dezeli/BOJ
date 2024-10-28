# ПЧЕЛИЧКАТА МАЯ

bees = list(map(int, input().split()))

avg_bees = sum(bees) // 3

print((avg_bees - bees[0]) * 2 + avg_bees - bees[1])
