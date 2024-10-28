# 어두운 건 무서워
import sys

input = sys.stdin.readline

R, C, Q = map(int, input().split())

sum_b = [[0 for _ in range(C + 1)]]

for _ in range(R):
    line = list(map(int, input().split()))
    sum_line = [0]
    sum_cnt = 0
    for i in range(C):
        sum_cnt += line[i]
        sum_line.append(sum_cnt + sum_b[-1][i + 1])
    sum_b.append(sum_line)


for _ in range(Q):
    r1, c1, r2, c2 = map(int, input().split())

    ans_sum = (
        sum_b[r2][c2] - sum_b[r2][c1 - 1] - sum_b[r1 - 1][c2] + sum_b[r1 - 1][c1 - 1]
    )
    amount = (c2 - c1 + 1) * (r2 - r1 + 1)
    print(ans_sum // amount)
