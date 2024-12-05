# 3n+1 수열

C = int(input())

cnt = 1
while C != 1:
    cnt += 1
    if C % 2 == 0:
        C //= 2
    else:
        C = C * 3 + 1

print(cnt)
