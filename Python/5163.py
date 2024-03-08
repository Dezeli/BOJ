# Isn’t It Funny How a Bear Likes Honey?
import math

K = int(input())
for i in range(1, K+1):
    b, w = map(float, input().split())
    helium = 0
    for __ in range(int(b)):
        r = float(input())
        helium += (4 * math.pi * (r**3)) / 3000

    print(f"Data Set {i}:")
    if helium>=w and b!=0:
        print("Yes")
    else:
        print("No")
    if i!=K:
        print()
