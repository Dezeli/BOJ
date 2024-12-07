

N = int(input())

zero = 0
for i in range(1, N+1):
    for j in str(i):
        if j=='0':
            zero += 1
print(zero)