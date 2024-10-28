# Sounds fishy!
import sys

F1 = int(sys.stdin.readline().rstrip())
F2 = int(sys.stdin.readline().rstrip())
F3 = int(sys.stdin.readline().rstrip())
F4 = int(sys.stdin.readline().rstrip())
if F1 > F2 > F3 > F4:
    print("Fish Diving")
elif F1 == F2 == F3 == F4:
    print("Fish At Constant Depth")
elif F1 < F2 < F3 < F4:
    print("Fish Rising")
else:
    print("No Fish")
