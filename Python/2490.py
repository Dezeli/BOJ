# 윷놀이

for _ in range(3):
    yoots = list(map(int, input().split()))
    if sum(yoots)==0:
        print('D')
    elif sum(yoots)==1:
        print('C')
    elif sum(yoots)==2:
        print('B')
    elif sum(yoots)==3:
        print('A')
    elif sum(yoots)==4:
        print('E')
