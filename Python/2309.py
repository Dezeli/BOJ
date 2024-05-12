# 일곱 난쟁이

tinymen = []
for _ in range(9):
    tinymen.append(int(input()))
tinymen.sort()

for i in range(9):
    for j in range(i + 1, 9):
        if sum(tinymen) - tinymen[i] - tinymen[j] == 100:
            fake = [i, j]
            break

for i in range(9):
    if i in fake:
        continue
    print(tinymen[i])
