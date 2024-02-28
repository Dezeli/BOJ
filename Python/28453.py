# Previous Level

N = int(input())
M = list(map(int, input().split()))

level = []

for i in M:
    if i==300:
        level.append(1)
    elif i>=275:
        level.append(2)
    elif i>=250:
        level.append(3)
    else:
        level.append(4)

print(*level)