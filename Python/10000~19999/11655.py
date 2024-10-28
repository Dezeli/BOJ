# ROT13

S = input()

for i in S:
    ord_i = ord(i)

    if 65 <= ord_i <= 90:
        ord_c = ord_i + 13
        if ord_c > 90:
            ord_c = ord_c - 26
        print(chr(ord_c), end="")
    elif 97 <= ord_i <= 122:
        ord_c = ord_i + 13
        if ord_c > 122:
            ord_c = ord_c - 26
        print(chr(ord_c), end="")
    else:
        print(i, end="")
