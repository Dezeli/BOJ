# Gahui and Soongsil University station

depth = 0

for i in range(4):
    how, step = input().split()
    step = int(step)

    if how == "Es":
        depth += step * 21
    else:
        depth += step * 17

print(depth)
