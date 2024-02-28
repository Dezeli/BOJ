# Area

n = int(input())

max_area = 0

for _ in range(n):
    h, w = map(int, input().split())
    max_area = max(max_area, h*w)
print(max_area)
