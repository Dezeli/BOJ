# 멀티탭 스케줄링
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
use = list(map(int, input().split()))

plug = set()
cnt = 0


def find_latest(i):
    global plug
    new_plug = set() | plug

    for num in use[i:]:
        new_plug -= {num}

        if len(new_plug) == 1:
            break
    plug -= {new_plug.pop()}


for i, num in enumerate(use):
    plug.add(num)
    if len(plug) > N:
        cnt += 1
        last = find_latest(i)
print(cnt)
