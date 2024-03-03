# Миша и негатив

n, m = map(int, input().split())

ori = []
rev = []

for i in range(n):
    line = input()
    ori.append(line)

next_line = input()
for i in range(n):
    line = input()
    rev.append(line)

cnt = 0
for i in range(n):
    for j in range(m):
        if ori[i][j] == rev[i][j]:
            cnt += 1
print(cnt)
