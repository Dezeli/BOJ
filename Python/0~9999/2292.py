# 벌집

N = int(input())

time = 0
multipleOfSixList = [i * 6 for i in range(1, 1600000)]
M = 1
i = 0
while N > M:
    M += multipleOfSixList[i]
    i += 1
    time += 1
print(time + 1)
