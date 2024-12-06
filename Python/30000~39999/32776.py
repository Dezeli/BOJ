# 가희와 4시간의 벽 2

S = int(input())
Ma, F, Mb = map(int, input().split())


if S<=240:
    print('high speed rail')
else:
    if Ma+F+Mb<S:
        print('flight')
    else:
        print('high speed rail')