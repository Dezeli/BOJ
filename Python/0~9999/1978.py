# 소수 찾기

T = int(input())

numList = list(map(int, input().split(" ")))
for i in range(2, 501):
    a = [j * i for j in range(2, 501)]
    numList = list(set(numList) - set(a))
numList.sort()
try:
    numList.remove(1)
except:
    pass
print(len(numList))
