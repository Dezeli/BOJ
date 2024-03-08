# 쌍의 합


T = int(input())
for _ in range(T):
    n = int(input())
    i = 1
    print("Pairs for %d:" %n, end = ' ')
    
    for k in range((n-1)//2):
        if k != 0:
            print(',', end = ' ')
        print(i, n-i, end = '')
        i += 1
        
    print()