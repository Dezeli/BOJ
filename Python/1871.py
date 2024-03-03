# 좋은 자동차 번호판
import sys

alp = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6,
    "H": 7,
    "I": 8,
    "J": 9,
    "K": 10,
    "L": 11,
    "M": 12,
    "N": 13,
    "O": 14,
    "P": 15,
    "Q": 16,
    "R": 17,
    "S": 18,
    "T": 19,
    "U": 20,
    "V": 21,
    "W": 22,
    "X": 23,
    "Y": 24,
    "Z": 25,
}

N = int(sys.stdin.readline().rstrip())
for _ in range(N):
    car = sys.stdin.readline().rstrip()
    alp_val = 0
    num_val = int(car[4:])
    for i in range(3):
        alp_val += alp[car[i]] * (26 ** (2 - i))

    if abs(alp_val - num_val) <= 100:
        print("nice")
    else:
        print("not nice")
