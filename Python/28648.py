# Торговый центр

n = int(input())

min_sum = 300

for i in range(n):
    t, l = map(int, input().split())

    min_sum = min(min_sum, t+l)

print(min_sum)