# Parenthesis

T = int(input())

for k in range(T):
    cover = True
    S = input()
    symbolList = []
    for i in S:
        if i == "(":
            symbolList.append(")")
        elif i == ")":
            try:
                symbolList.pop(-1)
            except:
                cover = False
                break
    if cover == True and len(symbolList) == 0:
        print("YES")
    else:
        print("NO")
