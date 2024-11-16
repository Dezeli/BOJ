# 알고리즘 수업 - 알고리즘의 수행 시간 4

n = int(input())

cnt = 0
for i in range(n - 1, -1, -1):
    cnt += i

print(cnt)
print(2)
