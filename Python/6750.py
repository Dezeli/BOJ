# Rotating letters

sign = ["I", "O", "S", "H", "Z", "X", "N"]

s = input()
cnt = 0
for i in s:
    if i in sign:
        cnt += 1

if cnt == len(s):
    print("YES")
else:
    print("NO")
