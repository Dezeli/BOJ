# 색종이 만들기
import sys

N = int(sys.stdin.readline().rstrip(" "))

papers = []
for _ in range(N):
    row = list(map(int, sys.stdin.readline().split(" ")))
    papers.append(row)

def check(root):
    stack = [root] 
    white = 0
    blue = 0
    while stack:
        color = 0
        x1, x2, y1, y2 = stack.pop()
        for y in range(y1, y2):
            color += sum(papers[y][x1:x2])

        if color == (x2-x1)*(y2-y1):
            blue += 1
        elif color == 0:
            white += 1
        else:
            stack.append([x1, (x1+x2)//2, y1, (y1+y2)//2])
            stack.append([x1, (x1+x2)//2, (y1+y2)//2, y2])
            stack.append([(x1+x2)//2, x2, y1, (y1+y2)//2])
            stack.append([(x1+x2)//2, x2, (y1+y2)//2, y2])
    return white, blue

white, blue = check([0, N, 0, N])

print(white)
print(blue)