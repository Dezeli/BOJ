# 명령 프롬프트
import sys

T = int(sys.stdin.readline().rstrip())
f_Word = [i for i in sys.stdin.readline().rstrip()]
for _ in range(T - 1):
    n_Word = sys.stdin.readline().rstrip()
    for i in range(len(n_Word)):
        if f_Word[i] != n_Word[i]:
            f_Word[i] = "?"
for i in f_Word:
    print(i, end="")