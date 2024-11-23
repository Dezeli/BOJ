# 남욱이의 닭장

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    print(2 * M - N, N - M)
