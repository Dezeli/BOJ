# 팩토리얼 0의 개수

N = int(input())
fac = 1
for i in range(1, N+1):
    fac *= i
    
cnt = 0
while fac%10==0:
    cnt += 1
    fac = fac//10
print(cnt)