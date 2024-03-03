# 지능형 기차 2

max_cnt = 0

cur = 0
for i in range(10):
    o, i = map(int, input().split())
    cur -= o
    cur += i
    max_cnt = max(max_cnt, cur)
print(max_cnt)
