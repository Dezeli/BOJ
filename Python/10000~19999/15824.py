# 너 봄에는 캡사이신이 맛있단다
import sys

input = sys.stdin.readline

N = int(input())
MOD = 1000000007

datas = sorted(list(map(int, input().split())))

def mul(a, b):
    if b==0:
        return 1
    if b==1:
        return a

    half = mul(a, b//2)

    if b%2==0:
        return half*half%MOD
    else:
        return half*half*a%MOD

sum_spicy = 0
for i in range(N):
    sum_spicy += datas[i]*(mul(2, i)-mul(2, N-i-1))

print(sum_spicy%MOD)