# Goodbye, Code Jam

T = int(input())
for i in range(1, T + 1):
    N = int(input())

    if N <= 25:
        print(f"Case #{i}: World Finals")
    elif N <= 1000:
        print(f"Case #{i}: Round 3")
    elif N <= 4500:
        print(f"Case #{i}: Round 2")
    else:
        print(f"Case #{i}: Round 1")
