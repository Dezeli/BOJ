# MBTI

jinho = input()

N = int(input())
cnt = 0

for _ in range(N):
    p = input()
    if p==jinho:
        cnt += 1

print(cnt)