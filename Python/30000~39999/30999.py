# 민주주의

N, M = map(int, input().split())
cnt = 0
for _ in range(N):
    S = input()
    correct = 0
    wrong = 0
    for i in S:
        if i == "O":
            correct += 1
        else:
            wrong += 1
    if correct > wrong:
        cnt += 1
print(cnt)
