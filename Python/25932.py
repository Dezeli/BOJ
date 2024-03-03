# Find the Twins

n = int(input())

for _ in range(n):
    players = list(map(int, input().split()))
    print(*players)
    if 17 in players and 18 in players:
        print("both")
    elif 17 in players:
        print("zack")
    elif 18 in players:
        print("mack")
    else:
        print("none")
    print()
