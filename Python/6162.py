# Superlatives

K = int(input())

for i in range(1, K+1):
    E, A = map(int, input().split())

    print(f"Data Set {i}:")
    if A>=E:
        print("no drought")
    else:
        mega = E/A
        n = 0
        while mega > 1 :
            mega /= 5
            n += 1
        print("mega "*(n-1) + "drought")
    print()