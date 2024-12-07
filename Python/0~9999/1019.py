# 책 페이지
import sys

input = sys.stdin.readline

N = int(input())
Nz = str(N)
cnt = [0 for _ in range(10)]
d = [0, 1, 20, 300, 4000, 50000, 600000, 7000000, 80000000, 900000000, 0]

digit = 0
left = 0
while N!=0:
    N, l = divmod(N, 10)

    for i in range(1, l):
        cnt[i] += 10**(digit)
    if l!=0:
        cnt[l] += left+1
    left += l*10**(digit)

    for i in range(1, 10):
        cnt[i] += d[digit]*l

    digit += 1


for i in range(1, len(Nz)):
    l, m, r = Nz[:-i], Nz[-i], Nz[-i+1:]
    if i>1 and m=='0':
        cnt[0] += (int(l)-1)*10**(i-1)
        cnt[0] += int(r)+1
    else:
        cnt[0] += int(l)*10**(i-1)


print(*cnt)