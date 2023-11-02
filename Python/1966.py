# 프린터 큐
import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split(" "))
    files = list(map(int, sys.stdin.readline().split(" ")))
    sort_files = sorted(files, reverse=True)

    importanceF = files[M]
    files[M] *= 10

    cnt = 0
    while True:
        if sort_files[0]*10 == files[0]:
            cnt += 1
            print(cnt)
            break
        if sort_files[0]==files[0]:
            sort_files.pop(0)
            files.pop(0)
            cnt += 1
        else:
            files.append(files.pop(0))