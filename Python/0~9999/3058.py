# 짝수를 찾아라


T = int(input())

for _ in range(T):
    min_num = 101
    sum_num = 0
    nums = list(map(int, input().split()))
    for n in nums:
        if n % 2 == 0:
            min_num = min(n, min_num)
            sum_num += n

    if sum_num:
        print(sum_num, min_num)
