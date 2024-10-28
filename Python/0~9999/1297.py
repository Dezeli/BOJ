# TV 크기
import sys

D, H, W = map(int, sys.stdin.readline().split(" "))
print(
    int(((D**2) * (H**2) / (H**2 + W**2)) ** 0.5),
    int(((D**2) * (W**2) / (H**2 + W**2)) ** 0.5),
)
