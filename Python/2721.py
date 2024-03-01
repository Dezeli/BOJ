# 삼각수의 합 

T = int(input())

for _ in range(T):
    n = int(input())
    result = 0
    for i in range(1, n+1):
        result += i*(i+1)*(i+2)//2
    print(result)