# 크로스워드
import sys

input = sys.stdin.readline

R, C = map(int, input().split())

lines = [input().rstrip() for _ in range(R)]
zip_lines = [''.join(i) for i in zip(*lines)]

words = []
for l in lines:
    words += l.split("#")
for l in zip_lines:
    words += l.split("#")

words.sort()
for i in words:
    if len(i)<2:
        continue
    print(i)
    break