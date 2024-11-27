# 서버

n, T = map(int, input().split())

work = 0
cnt = 0
for i in map(int, input().split()):
    work += i
    if work>T:
        break
    cnt += 1
print(cnt)
