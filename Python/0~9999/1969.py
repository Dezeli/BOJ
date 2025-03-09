# DNA
import sys
from collections import Counter

input = sys.stdin.readline

N, M = map(int, input().split())

DNA = [input().strip() for _ in range(N)]


min_d = ""
d = 0

for i in range(M):
    rev = [dna[i] for dna in DNA]
    freq = Counter(rev)
    c = sorted(freq.items(), key=lambda x: (-x[1], x[0]))[0][0]
    min_d += c
    d += sum(freq.values()) - freq[c]

print(min_d)
print(d)