# 그릇

S = input()
h = 10
last = S[0]

for i in S[1:]:
    if last == i:
        h += 5
    else:
        h += 10
    last = i
print(h)
