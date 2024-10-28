# K-세준수
import sys

N = int(sys.stdin.readline().rstrip())
K = int(sys.stdin.readline().rstrip())

nums = [0 for _ in range(N)]
for i in range(N):
    if i == 0:
        continue
    if nums[i] == 0:
        for j in range(i, N, i + 1):
            nums[j] = i + 1

cnt = 0
for i in nums:
    if i <= K:
        cnt += 1

print(cnt)
