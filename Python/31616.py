# 揃った文字 (Matched Letters)

N = int(input())
S = input()

c = S[0]
same = True
for i in S:
    if i!= c:
        same = False
        break
if same:
    print("Yes")
else:
    print("No")