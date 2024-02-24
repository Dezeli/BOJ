# ZOAC 6

N = int(input())

cnt = 0

for _ in range(N):
    S = input()
    if '01' in S or 'OI' in S:
        cnt += 1
print(cnt)