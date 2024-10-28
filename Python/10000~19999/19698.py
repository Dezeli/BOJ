# 헛간 청약

N, W, H, L = map(int, input().split())

can = (W // L) * (H // L)

if N < can:
    print(N)
else:
    print(can)
