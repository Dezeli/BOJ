# 쇠막대기

S = input()

stack = []

cnt = 0
bef = ')'
for i in S:
    if i=='(':
        stack.append(i)
    else:
        stack.pop()
        if bef=='(':
            cnt += len(stack)
        else:
            cnt += 1
    bef = i
print(cnt)