# 홀수

min_num = 101
sum_num = 0
for _ in range(7):
    n = int(input())
    if n % 2 == 1:
        sum_num += n
        min_num = min(min_num, n)

if sum_num == 0:
    print(-1)
else:
    print(sum_num)
    print(min_num)
