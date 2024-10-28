# Sticky Keys

s = input()

last = ""
for i in s:
    if last == i:
        continue
    print(i, end="")
    last = i
print()
