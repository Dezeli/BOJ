# Special Day
import sys

M = int(sys.stdin.readline().rstrip())
D = int(sys.stdin.readline().rstrip())

if M == 2 and D == 18:
    print("Special")
elif M == 2 and D > 18:
    print("After")
elif M > 2:
    print("After")
else:
    print("Before")
