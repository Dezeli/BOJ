# 수열의 변화
import sys

N, K = map(int, sys.stdin.readline().split())

original_list = list(map(int, sys.stdin.readline().split(",")))

for _ in range(K):
    for __ in range(len(original_list) - 1):
        original_list.append(original_list[1] - original_list[0])
        original_list.pop(0)
    original_list.pop(0)

result = ",".join(map(str, original_list))
print(result)
