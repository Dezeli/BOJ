# 브실이와 친구가 되고 싶어 🤸‍♀️

A, B = map(int, input().split())
K, X = map(int, input().split())

friend = 0
for i in range(A, B+1):
    if K-X<=i<=K+X:
        friend += 1

if friend:
    print(friend)
else:
    print("IMPOSSIBLE")