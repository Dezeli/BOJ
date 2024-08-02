# 문자가 몇갤까
import sys

input = sys.stdin.readline

while True:
    cnt = [0 for _ in range(100)]
    line = input().rstrip()
    if line=="#":
        break
    for i in line:
        cnt[ord(i.upper())] = 1
    print(sum(cnt[65:91]))