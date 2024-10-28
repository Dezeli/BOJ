# 세로읽기

words = []
lens = []
for _ in range(5):
    w = input()
    lens.append(len(w))
    words.append(w)

for i in range(max(lens)):
    for j in range(5):
        if i < lens[j]:
            print(words[j][i], end="")
print()
