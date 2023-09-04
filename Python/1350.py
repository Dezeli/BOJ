# 진짜 공간
import sys

N = int(sys.stdin.readline().rstrip())
files = list(map(int, sys.stdin.readline().rstrip().split()))
fileSize = int(sys.stdin.readline().rstrip())
saveSize = 0
for file in files:
    if file != 0:
        if file % fileSize != 0:
            saveSize += fileSize * (file // fileSize + 1)
        else:
            saveSize += fileSize * (file // fileSize)
print(saveSize)
