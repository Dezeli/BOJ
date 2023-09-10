# Growth Tips
import sys

tree = list(map(int, sys.stdin.readline().split()))
while tree != [0]:
    branch = 1
    leaf = 1
    for _ in range(tree[0]):
        leaf *= tree[branch]
        leaf -= tree[branch + 1]
        branch += 2
    print(leaf)
    tree = list(map(int, sys.stdin.readline().split()))
