# 개표

T = int(input())
for _ in range(T):
    n = int(input())
    draw = ['++++' for _ in range(n//5)]
    draw.append('|'*(n%5))
    print(*draw)

