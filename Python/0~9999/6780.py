# Sumac Sequences

t1 = int(input())
t2 = int(input())
cnt = 2
while t1 >= t2:
    cnt += 1
    t1, t2 = t2, t1 - t2

print(cnt)
