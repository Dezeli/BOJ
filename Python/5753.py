# Pascal Library

while True:
    N, D = map(int, input().split())

    if N==D==0:
        break
    
    dinners = [0 for _ in range(N)]
    for _ in range(D):
        dinner = list(map(int, input().split()))
        for i in range(N):
            dinners[i] += dinner[i]
    
    if max(dinners)==D:
        print("yes")
    else:
        print("no")