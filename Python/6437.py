# Golf

i = 0
while True:
    p, s = map(int, input().split())
    i += 1
    if p == s == 0:
        break

    print(f"Hole #{i}")
    if s == 1:
        print("Hole-in-one.")
    elif p - s >= 3:
        print("Double eagle.")
    elif p - s == 2:
        print("Eagle.")
    elif p - s == 1:
        print("Birdie.")
    elif p - s == 0:
        print("Par.")
    elif p - s == -1:
        print("Bogey.")
    elif p - s <= -2:
        print("Double Bogey.")

    print()
