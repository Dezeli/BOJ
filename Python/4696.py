# St. Ives

while True:
    num = float(input())

    if num == 0:
        break

    result = round(1 + num + num**2 + num**3 + num**4, 2)
    print("{:.2f}".format(result))
