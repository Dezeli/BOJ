# 최대공약수와 최소공배수

a, b = map(int, input().split())


def GCD(x, y):
    while y:
        x, y = y, x % y
    return x


def LCM(x, y):
    result = (x * y) // GCD(x, y)
    return result


print(GCD(a, b))
print(LCM(a, b))
