# 수학은 체육과목 입니다 2

n = int(input())%8+8

a = 1
result = 0

for _ in range(n):
    if result== 1:
        a = 1
    if result == 5:
        a = -1

    result += a

print(result)