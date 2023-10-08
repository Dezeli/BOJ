# 알파벳 개수

word = input()
alp = "abcdefghijklmnopqrstuvwxyz"
alp = list(alp)
for i in alp:
    cnt = word.count(i)
    print(cnt, end=" ")
