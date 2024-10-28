# Os últimos serão os primeiros

while True:
    N = int(input())
    if N == 0:
        break

    nums = []
    for _ in range(N):
        nums.append(int(input()))

    while nums:
        print(nums.pop())
    print(0)
