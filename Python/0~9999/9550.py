# 아이들은 사탕을 좋아해

T = int(input())


for _ in range(T):
    N, K = map(int, input().split())
    kids = 0
    candy = list(map(int, input().split()))
    for c in candy:
        kids += c // K
    print(kids)
