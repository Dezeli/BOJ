# 알고리즘 수업 - 알고리즘의 수행 시간 6

n = int(input())
sum = 0
num = n - 2
for i in range(1, n - 1):
    sum += num * i
    num -= 1

print(sum)
print(3)
