# 1
import sys

input = sys.stdin.readline
sys.set_int_max_str_digits(10**8)

one_list = [int("1" * i) for i in range(1, 10001)]


while True:
    try:
        n = int(input())
        for i in range(10000):
            if one_list[i] % n == 0:
                print(i + 1)
                break
    except:
        break
