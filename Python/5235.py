# Even Sum More Than Odd Sum

T = int(input())

for _ in range(T):
    nums = list(map(int, input().split()))[1:]
    odd = 0
    even = 0
    for i in nums:
        if i%2==0:
            even += i
        else:
            odd += i

    if odd<even:
        print("EVEN")
    elif odd==even:
        print("TIE")
    else:
        print("ODD")