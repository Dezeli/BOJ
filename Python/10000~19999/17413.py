# 단어 뒤집기 2

S = input()

stack = []

i = 0
while True:
    if i >= len(S):
        break

    if S[i] == "<":
        while stack:
            print(stack.pop(), end="")

        while S[i] != ">":
            print(S[i], end="")
            i += 1
        print(S[i], end="")
    elif S[i] == " ":
        while stack:
            print(stack.pop(), end="")
        print(S[i], end="")
    else:
        stack.append(S[i])
    i += 1


while stack:
    print(stack.pop(), end="")
print()
