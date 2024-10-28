# 앵그리 창영

N, W, H = map(int, input().split())

for _ in range(N):
    stick = int(input())

    if stick**2 <= (W**2 + H**2):
        print("DA")
    else:
        print("NE")
