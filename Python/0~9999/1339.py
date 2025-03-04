# 단어 수학
import sys

input = sys.stdin.readline

N = int(input())

words = []

for _ in range(N):
    words.append(input().rstrip())

ans = 0

dic={}

for w in words:
    cnt = len(w)
    for word in w:
        if word not in dic:
            dic[word] = (10**(cnt-1))
        else:
            dic[word] += (10**(cnt-1))
        cnt -= 1


values_lst = list(dic.values())
values_lst.sort()
values_lst.reverse()
num = 9

for i in values_lst:
    ans += i*num
    num -= 1    
print(ans)