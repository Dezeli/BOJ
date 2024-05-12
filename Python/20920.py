# 영단어 암기는 괴로워
import sys
from collections import defaultdict

input = sys.stdin.readline

word_dict = defaultdict(int)

N, M = map(int, input().split())

for i in range(1, N + 1):
    s = input().rstrip()
    if len(s) >= M:
        word_dict[s] += 1

words = []
for key, val in word_dict.items():
    words.append([val, key])

words.sort(key=lambda x: (-x[0], -len(x[1]), x[1]))

for n, w in words:
    print(w)
