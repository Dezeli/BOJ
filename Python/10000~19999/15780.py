# 멀티탭 충분하니?

N, K = map(int, input().split())

tabs = list(map(int, input().split()))
cnt = 0
for i in tabs:
    cnt += (i + 1) // 2

if cnt >= N:
    print("YES")
else:
    print("NO")
