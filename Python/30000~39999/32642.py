# 당구 좀 치자 제발

N = int(input())

mad = 0
sum_mad = 0
for i in list(map(int, input().split())):
    if i==0:
        mad -= 1
    else:
        mad +=1
    sum_mad += mad
print(sum_mad)