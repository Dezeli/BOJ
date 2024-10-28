# IOIOI
import sys
from collections import defaultdict

N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
S = sys.stdin.readline().rstrip()

find = "I" + ("OI" * N)


def kmp(S, pattern):
    table = [0 for _ in range(len(pattern))]
    i = 0
    for j in range(1, len(pattern)):
        while i > 0 and pattern[i] != pattern[j]:
            i = table[i - 1]

        if pattern[i] == pattern[j]:
            i += 1
            table[j] = i

    cnt = 0
    i = 0
    for j in range(len(S)):
        while i > 0 and pattern[i] != S[j]:
            i = table[i - 1]

        if pattern[i] == S[j]:
            i += 1
            if i == len(pattern):
                cnt += 1
                i = table[i - 1]

    return cnt


print(kmp(S, find))
