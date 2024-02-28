# Планеты двух измерений

N, M = map(int, input().split())

if N>M:
    print(2*M+1)
elif N<M:
    print(2*N+1)
else:
    print(N+M)