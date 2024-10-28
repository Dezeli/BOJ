# 암호 만들기
import sys

input = sys.stdin.readline


def bt(cnt, idx):
    if cnt == L:
        vo, co = 0, 0
        for i in range(L):
            if ans[i] in consonant:
                vo += 1
            else:
                co += 1
        if vo >= 1 and co >= 2:
            print("".join(ans))
        return

    for i in range(idx, C):
        ans.append(words[i])
        bt(cnt + 1, i + 1)
        ans.pop()


L, C = map(int, input().split())
words = input().rstrip().split()
words.sort()
consonant = ["a", "e", "i", "o", "u"]
ans = []
bt(0, 0)
