# Times17
import sys

binaryNum = "0b" + str(sys.stdin.readline().rstrip())

print(format(int(binaryNum, 2) * 17, "b"))
