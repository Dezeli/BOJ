# 팩토리얼

N = int(input())

factorial = 1
for i in range(2, N + 1):
    factorial *= i
print(factorial)
