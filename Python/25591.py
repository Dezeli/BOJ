# 푸앙이와 종윤이

A, B = map(int, input().split())

a = 100-A
b = 100-B
c = 100 -(a+b)
d = a*b

result = c*100 + d
q = result//100-c
r = d%100

print(a, b, c, d, q, r)
print(result//100, result%100)