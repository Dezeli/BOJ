# Palindrome Numbers
import sys

num = sys.stdin.readline().rstrip()
while int(num):
    check = True
    for i in range(len(num) // 2):
        if num[i] != num[-i - 1]:
            check = False
            break
    if check:
        print("yes")
    else:
        print("no")
    num = sys.stdin.readline().rstrip()
    