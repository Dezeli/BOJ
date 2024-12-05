# 고려대학교에는 공식 와인이 있다

C, K, P = map(int, input().split())

wine = 0
for n in range(1, C + 1):
    wine += K * n + P * n * n

print(wine)
