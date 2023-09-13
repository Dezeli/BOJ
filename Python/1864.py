# Octopus Numbers
import sys

oct_to_int = {"-": 0, "\\": 1, "(": 2, "@": 3, "?": 4, ">": 5, "&": 6, "%": 7, "/": -1}

oct_num = sys.stdin.readline().rstrip()

while oct_num != "#":
    oct_mul = len(oct_num) - 1
    num = 0
    for i in oct_num:
        num += 8**oct_mul * oct_to_int[i]
        oct_mul -= 1
    print(num)

    oct_num = sys.stdin.readline().rstrip()