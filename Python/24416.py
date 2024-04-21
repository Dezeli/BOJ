# 알고리즘 수업 - 피보나치 수 1

n = int(input())
cnt1 = 1

def fib(n):
    global cnt1
    if n==1 or n==2:
        return 1
    else:
        cnt1 += 1
        return fib(n-1) + fib(n-2)
fib(n)
print(cnt1, n-2)