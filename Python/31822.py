# 재수강

re = input()[:5]
N = int(input())
cnt = 0
for _ in range(N):
    code = input()
    if code[:5] == re:
        cnt += 1

print(cnt)
