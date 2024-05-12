# 소수의 연속합

import math

N = int(input())

if N == 1:
    print(0)
else:
    aristo = [True] * (N + 1)
    aristo[0] = False
    aristo[1] = False

    for i in range(2, int(math.sqrt(N) + 1)):
        if aristo[i] == True:
            j = 2
            while (i * j) <= N:
                aristo[i * j] = False
                j += 1

    prime_list = []
    for i in range(2, N + 1):
        if aristo[i] == True:
            prime_list.append(i)

    l = 0
    r = 0
    sum_prime = prime_list[0]
    cnt = 0

    while l <= r:

        if sum_prime > N:
            sum_prime -= prime_list[l]
            l += 1
        else:
            if sum_prime == N:
                cnt += 1
            r += 1
            if r == len(prime_list):
                break
            sum_prime += prime_list[r]

    print(cnt)
