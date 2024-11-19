# ZOAC 4

H, W, N, M = map(int, input().split())

a, b = divmod(H, N+1)
c, d = divmod(W, M+1)
if b>0:
    a += 1
if d>0:
    c += 1
print(a*c)
