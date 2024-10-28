# IBM 빼기 1

n = int(input())

for i in range(1, n + 1):
    print(f"String #{i}")
    word = input()
    for s in word:
        if s == "Z":
            print("A", end="")
        else:
            print(chr(ord(s) + 1), end="")

    print()
    print()
