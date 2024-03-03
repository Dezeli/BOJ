# 카드 뽑기

N, M, K = map(int, input().split())

print(min(M, K) + min(N - M, N - K))
