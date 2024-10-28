# House Numbers
import sys

while True:
    num = sys.stdin.readline().rstrip()
    if num == "0":
        break
    size = 1
    for i in num:
        if i == "0":
            size += 5
        elif i == "1":
            size += 3
        else:
            size += 4
    print(size)
