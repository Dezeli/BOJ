# 랜선 자르기
import sys

K, N = map(int, sys.stdin.readline().split(" "))
lines = []
for _ in range(K):
    line = int(sys.stdin.readline().rstrip())
    lines.append(line)

start = 1
end = max(lines) + 1

while start + 1 < end:
    mid = (start + end) // 2
    cut = 0
    for line in lines:
        cut += line // mid
    if cut >= N:
        start = mid
    else:
        end = mid

print(start)
