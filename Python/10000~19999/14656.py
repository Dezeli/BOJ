# 조교는 새디스트야!!

N = int(input())
line = list(map(int, input().split()))

cnt = 0
for i in range(N):
    if line[i] != i + 1:
        cnt += 1

print(cnt)
