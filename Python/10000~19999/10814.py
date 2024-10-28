# 나이순 정렬

N = int(input())

userDict = {}
for i in range(1, 201):
    userDict[i] = []
for i in range(N):
    a, b = input().split()
    userDict[int(a)].append(b)
for i in range(1, 201):
    for j in userDict[i]:
        print(i, j)
