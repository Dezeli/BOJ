# 탁구 경기

N = int(input())

X = 0
Y = 0

for _ in range(N):
    s = input()
    if s=='D':
        X += 1
    else:
        Y += 1

    if abs(X-Y)>=2:
        break

print(f"{X}:{Y}")