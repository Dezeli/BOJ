# 조합 (Combination)
import sys

input = sys.stdin.readline

N, R = map(int, input().split())

MOD = 1000000007
fac = [0, 1]


f = 1
for i in range(2, N+1):
    f *= i
    f %= MOD
    fac.append(f)


power_dict = {}
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
    
if R==0 or N==R:
    print(1)
else:
    print(fac[N]*power(fac[N-R]*fac[R]%MOD, MOD-2)%MOD)