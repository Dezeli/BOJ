# Four Squares
import sys

n = int(sys.stdin.readline().rstrip())
squares = [i**2 for i in range(int(n ** (1 / 2)), 0, -1)]


def find(n):
    if n in squares:
        return 1

    for i in squares:
        if (n - i) in squares:
            return 2

    for i in squares:
        for j in squares:
            if (n - i - j) in squares:
                return 3
    return 4


print(find(n))
