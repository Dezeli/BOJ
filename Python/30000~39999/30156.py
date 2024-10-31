# Malvika is peculiar about color of balloons

T = int(input())

for _ in range(T):
    s = input()
    a = s.count('a')
    b = s.count('b')
    print(min(a, b))