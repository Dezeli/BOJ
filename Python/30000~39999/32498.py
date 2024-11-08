# Call for Problems

n = int(input())

cnt = 0
for _ in range(n):
    d = int(input())
    if d % 2 == 1:
        cnt += 1

print(cnt)
