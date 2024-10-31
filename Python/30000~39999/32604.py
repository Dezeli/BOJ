# Jumbled Scoreboards

n = int(input())

result = True
a1, b1 = map(int, input().split())
for _ in range(n-1):
    a2, b2 = map(int, input().split())
    if not (a1<=a2 and b1<=b2):
        result = False
    a1, b1 = a2, b2

if result:
    print("yes")
else:
    print("no")

