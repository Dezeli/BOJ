# Vowel Count

T = int(input())
for _ in range(T):
    S = input()

    cnt = 0
    for i in S:
        if i=='a' or i=='o' or i=='i' or i=='u' or i=='e':
            cnt += 1
    print(S)
    if cnt*2>len(S):
        print(1)
    else:
        print(0)