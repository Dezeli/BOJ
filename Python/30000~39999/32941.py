# 왜 맘대로 예약하냐고

T, X = map(int, input().split())
N = int(input())

cnt = 0
for _ in range(N):
    K = int(input()) 
    A = list(map(int, input().split()))
    if X in A:
        cnt += 1

if cnt==N:
    print("YES")
else:
    print("NO")