# 저항
import sys

c1 = sys.stdin.readline().rstrip()
c2 = sys.stdin.readline().rstrip()
c3 = sys.stdin.readline().rstrip()
color = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9,
}
print(int(str(color[c1]) + str(color[c2])) * (10 ** color[c3]))
