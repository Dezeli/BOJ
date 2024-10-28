# Máquina de café
# 포르투갈어 문제
import sys

num1 = int(sys.stdin.readline().rstrip())
num2 = int(sys.stdin.readline().rstrip())
num3 = int(sys.stdin.readline().rstrip())
print(min([num1 * 2 + num2, num1 + num3, num3 * 2 + num2]) * 2)
