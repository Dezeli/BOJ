# 모비스

S = input()
check = [0 for _ in range(5)]

for i in S:
    if i == "M":
        check[0] = 1
    if i == "O":
        check[1] = 1
    if i == "B":
        check[2] = 1
    if i == "I":
        check[3] = 1
    if i == "S":
        check[4] = 1
if sum(check) == 5:
    print("YES")
else:
    print("NO")
