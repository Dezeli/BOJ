# Floppies


i = 0
file = 62*30000
while True:
    s = int(input())
    i += 1
    if s==0:
        break
    
    print(f"File #{i}")

    if s%2==0:
        s = s//2
    else:
        s = s//2 + 1
    if s%2==0:
        s += s//2
    else:
        s += s//2 + 1
    cnt = (s+(file - 1))//file
    print(f"John needs {cnt} floppies.")
    print()