# 치킨댄스를 추는 곰곰이를 본 임스 2

N = int(input())

cnt = 0
for _ in range(N):
    d, num = input().split("-")
    if int(num) <= 90:
        cnt += 1
print(cnt)
