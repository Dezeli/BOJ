# Head or Tail

while True:
    N = int(input())
    if N==0:
        break
    R = list(map(int, input().split()))

    M = 0
    J = 0
    for i in R:
        if i==0:
            M += 1
        else:
            J += 1
    print(f"Mary won {M} times and John won {J} times")