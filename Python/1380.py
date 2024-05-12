# 귀걸이

scenario = 0
while True:
    scenario += 1
    n = int(input())
    if n == 0:
        break
    names = [0] + [input() for _ in range(n)]
    cnt = [0 for _ in range(n + 1)]
    for _ in range(n * 2 - 1):
        a, b = input().split()
        cnt[int(a)] += 1
    for i in range(1, n + 1):
        if cnt[i] == 1:
            print(scenario, names[i])
            break
