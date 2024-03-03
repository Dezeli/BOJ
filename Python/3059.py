# 등장하지 않는 문자의 합

T = int(input())
for _ in range(T):
    ascii_sum = 2015
    s = input()
    same = []
    for i in s:
        if i not in same:
            ascii_sum -= ord(i)
            same.append(i)
    print(ascii_sum)
