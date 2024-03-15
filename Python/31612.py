# 画数数え (Stroke Count) 

N = int(input())
S = input()
cnt = 0
for i in S:
    if i=='o':
        cnt += 1
    else:
        cnt += 2
print(cnt)