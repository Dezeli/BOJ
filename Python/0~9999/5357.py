# Dedupe

T = int(input())
for _ in range(T):
    s = input()
    last = ""
    for i in s:
        if i == last:
            continue
        else:
            print(i, end="")
        last = i
    print()
