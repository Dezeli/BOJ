# Triangle Times
import sys

num1 = int(sys.stdin.readline().rstrip())
num2 = int(sys.stdin.readline().rstrip())
num3 = int(sys.stdin.readline().rstrip())
if num1 == 60 and num2 == 60 and num3 == 60:
    print("Equilateral")
elif num1 + num2 + num3 == 180:
    if num1 != num2 and num2 != num3 and num3 != num1:
        print("Scalene")
    else:
        print("Isosceles")
else:
    print("Error")
