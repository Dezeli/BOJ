# 균형잡힌 세상

s = input()
while s != ".":
    quene = [0]
    result = "yes"
    for i in s:
        if i == "[" or i == "(":
            quene.append(i)
        elif i == "]":
            if quene.pop() != "[":
                result = "no"
                break
        elif i == ")":
            if quene.pop() != "(":
                result = "no"
                break
    if quene != [0]:
        result = "no"
    print(result)
    s = input()
