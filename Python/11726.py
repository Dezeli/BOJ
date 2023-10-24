# 2×n 타일링

n = int(input())

quotient = n // 2
times = 0
while quotient > -1:
    num = n - (2 * quotient)
    time = 1
    for i in range(1, num + quotient + 1):
        time *= i
    for j in range(1, num + 1):
        time //= j
    for k in range(1, quotient + 1):
        time //= k
    times += time
    quotient -= 1
print(int(times) % 10007)
