# 숫자 카드 2
import collections

N = int(input())
cards = list(map(int, input().split()))

M = int(input())
check_list = list(map(int, input().split()))

cards_dict = collections.defaultdict(int)
for card in cards:
    cards_dict[card] += 1

for check in check_list:
    print(cards_dict[check], end=" ")
