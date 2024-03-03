# Hangover

while True:
    n = float(input())
    if n == 0:
        break

    card_len = 0
    i = 1
    while n > card_len:
        i += 1
        card_len += 1 / i

    print(i - 1, "card(s)")
