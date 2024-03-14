# 現れている数字 (Appearing Numbers)

N = int(input())
A = list(set(map(int, input().split())))
A.sort()

for i in A:
    print(i)

