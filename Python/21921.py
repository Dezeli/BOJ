# 블로그
import sys

input = sys.stdin.readline

N, X = map(int, input().split())

blog = list(map(int, input().split()))
sum_blog = [0]

for i in blog:
    sum_blog.append(sum_blog[-1] + i)

max_vistor = 0
cnt = 1

for i in range(N - X + 1):
    cur = sum_blog[i + X] - sum_blog[i]
    if max_vistor < cur:
        cnt = 1
        max_vistor = cur
    elif max_vistor == cur:
        cnt += 1

if max_vistor:
    print(max_vistor)
    print(cnt)
else:
    print("SAD")
