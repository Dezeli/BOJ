# 소수 구하기

M, N = map(int, input().split())

def isPrime(m, n):
    n += 1
    prime = [0] * n
    for i in range(2, int(n ** (1 / 2)) + 1):
        if prime[i] == 0:
            for j in range(2 * i, n, i):
                prime[j] = 1

    for i in range(m, n):
        if i > 1 and prime[i] == 0:
            print(i)

isPrime(M, N)
