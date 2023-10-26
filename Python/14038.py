# Tournament Selection
import sys

result = []
for _ in range(6):
    result.append(sys.stdin.readline().rstrip())
if result.count("W") > 4:
    print(1)
elif result.count("W") > 2:
    print(2)
elif result.count("W") > 0:
    print(3)
else:
    print(-1)
