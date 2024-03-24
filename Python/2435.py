# 기상청 인턴 신현수
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
temps = list(map(int, input().split()))
sum_temp = [0]

for i in temps:
    sum_temp.append(sum_temp[-1] + i)

max_temp = -100*K

for i in range(N-K+1):
    max_temp = max(max_temp, sum_temp[i+K]-sum_temp[i])
print(max_temp)