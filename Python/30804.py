# 과일 탕후루
import sys

input = sys.stdin.readline

sys.setrecursionlimit(10**6)


N = int(input())
S = list(map(int, input().split()))
num = [0] * 10

max_num = 0

def tanghuru(start, end, kind):
    global N
    global max_num
    if end == N:
        return 0
    
    num[S[end]] += 1
    if num[S[end]] == 1:
        kind += 1
        
    if kind > 2:
        num[S[start]] -= 1
        if num[S[start]] == 0:
            kind -= 1
        start += 1
    
    max_num = max(max_num, end - start + 1)
    return tanghuru(start, end+1, kind)
    
tanghuru(0, 0, 0)

print(max_num)