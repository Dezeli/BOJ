# N포커

N = int(input())

MOD = 10007

if N < 4:
    print(0)
else:
    sum_case = 0
    for i in range(1, N//4+1):
        c = 1
        for j in range(i):
            c *= 13-j
            c //= j+1
            c %= MOD
        for j in range(N-4*i):
            c *= 52-(4*i)-j
            c //= j+1
        c %= MOD

        if i%2==1:
            sum_case += c
        else:
            sum_case -= c

        sum_case %= MOD
    print(sum_case)