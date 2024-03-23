# 홀수일까 짝수일까

N = int(input())

for _ in range(N):
    K = int(input())
    if K%2==0:
        print("even")
    else:
        print("odd")