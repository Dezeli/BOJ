# 공 넣기

N, M = map(int, input().split())


bag = [0 for i in range(N+1)]
for _ in range(M):
    i, j, k = map(int, input().split())
    for b in range(i, j+1):
        bag[b] = k

print(*bag[1:])
