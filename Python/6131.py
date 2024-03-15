# 완전 제곱수

N = int(input())

nums = [i**2 for i in range(1, 501)]

cnt = 0
for i in nums:
    for j in nums:
        if i-j==N:
            cnt += 1
print(cnt)