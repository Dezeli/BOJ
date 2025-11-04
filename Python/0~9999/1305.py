# 광고
import sys

input = sys.stdin.readline

L = int(input())
s = input().strip()

lps = [0] * L
j = 0

for i in range(1, L):
    while j > 0 and s[i] != s[j]:
        j = lps[j-1]
    if s[i] == s[j]:
        j += 1
        lps[i] = j

print(L - lps[-1])
