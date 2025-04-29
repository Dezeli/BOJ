# 이항 계수 3
import sys

input = sys.stdin.readline

M = int(input())
MOD = 1000000007
fac = [0, 1]


f = 1
for i in range(2, 4000000+1):
    f *= i
    f %= MOD
    fac.append(f)



def power(a, p):
    if p==1:
        return a
    if p in power_dict:
        return power_dict[p]
    
    if p%2==0:
        power_dict[p] =  power(a, p//2)*power(a, p//2)%MOD
        return power_dict[p]
    else:
        power_dict[p] =  power(a, p//2)*power(a, p//2)*power(a, 1)%MOD
        return power_dict[p]

for i in range(M):
    power_dict = {}
    N, K = map(int, input().split())
    if K==0 or N==K:
        print(1)
    else:
        print(fac[N]*power(fac[N-K]*fac[K]%MOD, MOD-2)%MOD)