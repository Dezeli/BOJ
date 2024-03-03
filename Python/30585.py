# Поп-ит

h, w = map(int, input().split())

r = 0
b = 0

for _ in range(h):
    line = input()
    for i in line:
        if i == "0":
            r += 1
        else:
            b += 1
print(min(r, b))
