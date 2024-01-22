# 母音を数える (Counting Vowels)

N = int(input())
S = input()
cnt = 0
vowels = ['a', 'e', 'i', 'o', 'u']


for i in S:
    if i in vowels:
        cnt += 1

print(cnt)