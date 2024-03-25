import sys

Ns = list(map(int, sys.stdin.read().split()))

for n in Ns:
    if n==0:
        break
    result = []
    for i in range(1, int(n**(1/2))+1):
        if n%i==0:
            result.append(i)
            if i < n//i:
                result.append(n//i)
    
    if sum(result)-n == n:
        print(n, "PERFECT")
    elif sum(result)-n > n:
        print(n, "ABUNDANT")
    else:
        print(n, "DEFICIENT")