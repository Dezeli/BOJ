# Speed fines are not fine!
import sys

L = int(sys.stdin.readline().rstrip())
S = int(sys.stdin.readline().rstrip())
if 1 <= S - L <= 20:
    print("You are speeding and your fine is $100.")
elif 21 <= S - L <= 30:
    print("You are speeding and your fine is $270.")
elif 31 <= S - L:
    print("You are speeding and your fine is $500.")
else:
    print("Congratulations, you are within the speed limit!")
