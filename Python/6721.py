# Backward numbers

for _ in range(int(input())):
    a, b = input().split()
    a = a[::-1]
    b = b[::-1]
    result = int(a) + int(b)
    print(int(str(result)[::-1]))