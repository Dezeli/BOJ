# No Brainer

n = int(input())
for _ in range(n):
    brain, zombies = map(int, input().split())
    if brain >= zombies:
        print("MMM BRAINS")
    else:
        print("NO BRAINS")