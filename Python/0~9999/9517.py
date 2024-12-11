# 아이 러브 크로아티아

K = int(input())
N = int(input())

sum_t = 0
for _ in range(N):
    T, Z = input().split()
    sum_t += int(T)

    if 210<=sum_t:
        K %= 8
        if K==0:
            K = 8
        print(K)
        break

    if Z=='T':
        K += 1