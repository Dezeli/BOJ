# A와 B
import sys

input = sys.stdin.readline

S = input().rstrip()
T = input().rstrip()

remove_list = []
for i in T:
    remove_list.append(i)

pos = False
while remove_list:
    if ''.join(remove_list)==S:
        print(1)
        pos = True
        break
    l = remove_list.pop()
    if l=='B':
        remove_list.reverse()
if not pos:
    print(0)
