# 문자열

A, B = input().split()

min_cnt = len(B)
for i in range(len(B) - len(A) + 1):
    cnt = 0
    for j in range(i, i + len(A)):
        if A[j - i] != B[j]:
            cnt += 1
    min_cnt = min(cnt, min_cnt)
print(min_cnt)
