# 더하기 사이클

N = int(input())
answer = N
cnt = 0
while True:
    N1 = int(N / 10)
    N2 = int(N % 10)
    N3 = N1 + N2
    N4 = N3 % 10
    N = 10 * N2 + N4
    cnt += 1
    if N == answer:
        break
print(cnt)