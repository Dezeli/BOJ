# 한수

N = int(input())

hanNum = 0
for i in range(1, N + 1):
    if i > 99:
        i_str = str(i)
        diff = int(i_str[1]) - int(i_str[0])
        for k in range(2, len(i_str)):
            if int(i_str[k]) != int(i_str[k - 1]) + diff:
                hanNum -= 1
                break
    hanNum += 1
print(hanNum)
