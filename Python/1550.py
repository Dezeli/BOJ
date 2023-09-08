# 16진수
import sys

num = sys.stdin.readline().rstrip()
num = num[::-1]
numDict = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15,
}
multiply = 1
decimal = 0
for i in num:
    decimal += numDict[i] * multiply
    multiply *= 16
print(decimal)
