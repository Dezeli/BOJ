# 문자열 분석

while True:
    try:
        upper = 0
        lower = 0
        number = 0
        blank = 0
        S = input()
        for i in S:
            if i == " ":
                blank += 1
            elif i.isupper():
                upper += 1
            elif i.islower():
                lower += 1
            else:
                number += 1
        print(lower, upper, number, blank)
    except:
        break
