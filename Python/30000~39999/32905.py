# RACI

n, m = map(int, input().split())

flag = True

for _ in range(n):
    line = list(input().split())

    if line.count("A") != 1:
        flag = False

if flag:
    print('Yes')
else:
    print('No')