# Multiple Choice

N = int(input())
A1 = [input() for _ in range(N)]
A2 = [input() for _ in range(N)]

cnt = 0
for i in range(N):
    if A1[i] == A2[i]:
        cnt += 1
print(cnt)
