# Peter's smokes
import sys

while True:
    try:
        k, n = map(int, sys.stdin.readline().split())
        chicken = 0
        while True:
            a, b = divmod(k, n)
            if a == 0:
                chicken += b
                break
            else:
                chicken += a * n
                k = a + b
        print(chicken)
    except:
        break
