# 단어 뒤집기

T = int(input())
for _ in range(T):
    s = list(input().split())

    for i in s[:-1]:
        print(i[::-1], end=" ")
    print(s[-1][::-1])
