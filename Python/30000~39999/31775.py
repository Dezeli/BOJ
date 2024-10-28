# 글로벌 포닉스

S1 = input()
S2 = input()
S3 = input()

g = ["k", "l", "p"]
f = [S1[0], S2[0], S3[0]]
f.sort()

if g == f:
    print("GLOBAL")
else:
    print("PONIX")
