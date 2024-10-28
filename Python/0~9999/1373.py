# 2진수 8진수
import sys

binary = int("0b" + sys.stdin.readline().rstrip(), 2)
octal = oct(binary)
print(octal[2:])
