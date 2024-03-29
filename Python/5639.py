# 이진 검색 트리
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

nodes = []
while True:
    try:
        nodes.append(int(input()))
    except:
        break


def post(start, end):
    if start > end:
        return
    mid = end + 1
    for i in range(start + 1, end + 1):
        if nodes[i] > nodes[start]:
            mid = i
            break
    post(start + 1, mid - 1)
    post(mid, end)
    print(nodes[start])


post(0, len(nodes) - 1)
