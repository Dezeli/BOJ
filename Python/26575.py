# Pups

n = int(input())
for _ in range(n):
    d, f, p = map(float, input().split())
    result = round(d*f*p, 2)
    print("${:.2f}".format(result))