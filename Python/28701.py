# 세제곱의 합

N = int(input())

print(sum([i for i in range(1, N+1)]))
print(sum([i for i in range(1, N+1)])**2)
print(sum([i**3 for i in range(1, N+1)]))