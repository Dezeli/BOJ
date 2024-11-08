# 로마 숫자 만들기
import sys
from itertools import combinations_with_replacement

input = sys.stdin.readline

nums = [1, 5, 10, 50]
N = int(input())

make = set([sum(i) for i in combinations_with_replacement(nums, N)])

print(len(make))
