# 숫자 카드
import sys

input = sys.stdin.readline

N = int(input())
cards = sorted(list(map(int, input().split())))

M = int(input())
nums = list(map(int, input().split()))


def search(num):
    l = 0
    r = N - 1
    while l <= r:
        mid = (l + r) // 2
        if cards[mid] == num:
            return 1
        elif cards[mid] < num:
            l = mid + 1
        else:
            r = mid - 1
    return 0


print(*[search(i) for i in nums])
