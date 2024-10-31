# Cookie Piles

T = int(input())

for _ in range(T):
    N, A, D = map(int, input().split())
    sum_num = 0
    num = A
    for __ in range(N):
        sum_num += num
        num += D
    print(sum_num)