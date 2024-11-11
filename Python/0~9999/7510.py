# 고급수학


n = int(input())

for i in range(1, n+1):
    print(f"Scenario #{i}:")

    l = list(map(int, input().split()))

    if max(l)**2*2==sum([i**2 for i in l]):
        print("yes")
    else:
        print("no")
    print()