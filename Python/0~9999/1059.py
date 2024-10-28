# 좋은 구간

L = int(input())
S = list(map(int, input().split()))
n = int(input())

S.sort()

cnt = 0
if n < S[0]:
    for i in range(1, S[0]):
        for j in range(i + 1, S[0]):
            if i <= n <= j:
                cnt += 1
else:
    for a in range(len(S) - 1):
        if n > S[a + 1]:
            continue

        for i in range(S[a] + 1, S[a + 1]):
            for j in range(i + 1, S[a + 1]):
                if i <= n <= j:
                    cnt += 1
        break
print(cnt)
