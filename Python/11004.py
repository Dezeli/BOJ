# K번째 수

N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
print(A[K - 1])
