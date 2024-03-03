# The Walking Adam

T = int(input())

for _ in range(T):
    cnt = 0
    s = input()
    for i in s:
        if i == "U":
            cnt += 1
        else:
            break
    print(cnt)
