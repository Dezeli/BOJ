# 블랙잭
import itertools

N, M = map(int, input().split())

cards = list(map(int, input().split()))
combins = list(itertools.combinations(cards, 3))

jack = 0
for combin in combins:
    if sum(combin) <= M:
        jack = max([jack, sum(combin)])

print(jack)