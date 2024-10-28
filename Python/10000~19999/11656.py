# 접미사 배열

S = input()
jup = []

for i in range(len(S)):
    jup.append(S[i:])
jup.sort()

for i in jup:
    print(i)
