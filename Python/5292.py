# Counting Swann’s Coins

coin = int(input())

for i in range(1, coin + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("DeadMan")
    elif i % 3 == 0:
        print("Dead")
    elif i % 5 == 0:
        print("Man")
    else:
        print(i, end=" ")
