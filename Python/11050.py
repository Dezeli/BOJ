# 이항 계수 1
import itertools

N, K = map(int, input().split())
Nlist = [0 for _ in range(N)]

print(len(list(itertools.combinations(Nlist, K))))