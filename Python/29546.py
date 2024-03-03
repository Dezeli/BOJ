# Файлы

n = int(input())

files = [0]
for _ in range(n):
    files.append(input())

m = int(input())
for _ in range(m):
    l, r = map(int, input().split())
    for i in range(l, r + 1):
        print(files[i])
