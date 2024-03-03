# 하얀 칸
import sys

l1 = sys.stdin.readline().rstrip()
l2 = sys.stdin.readline().rstrip()
l3 = sys.stdin.readline().rstrip()
l4 = sys.stdin.readline().rstrip()
l5 = sys.stdin.readline().rstrip()
l6 = sys.stdin.readline().rstrip()
l7 = sys.stdin.readline().rstrip()
l8 = sys.stdin.readline().rstrip()
odd = [l2, l4, l6, l8]
even = [l1, l3, l5, l7]
cnt = 0
for line in odd:
    for i in range(len(line)):
        if i % 2 == 1 and line[i] == "F":
            cnt += 1


for line in even:
    for i in range(len(line)):
        if i % 2 == 0 and line[i] == "F":
            cnt += 1
print(cnt)
