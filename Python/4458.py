# 첫 글자를 대문자로

N = int(input())

for _ in range(N):
    s = input()
    print(s[0].upper() + s[1:])
