# Checkerboard Rows

T = int(input())

for _ in range(T):
    checker = list(map(int, input().split()))[1:]

    cnt = [0 for _ in range(9)]
    for i in range(len(checker)):
        if i%2==0:
            continue
        else:
            cnt[checker[i]] += 1
    print(max(cnt))