# Divide the Cash

n, d = map(int, input().split())
per = []

for _ in range(n):
    per.append(int(input()))

for i in per:
    print(d * i // sum(per))
