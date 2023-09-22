# 36진수
import sys
from collections import defaultdict

N = int(sys.stdin.readline().rstrip())

nums = []
nums_36_dict = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15,
    "G": 16,
    "H": 17,
    "I": 18,
    "J": 19,
    "K": 20,
    "L": 21,
    "M": 22,
    "N": 23,
    "O": 24,
    "P": 25,
    "Q": 26,
    "R": 27,
    "S": 28,
    "T": 29,
    "U": 30,
    "V": 31,
    "W": 32,
    "X": 33,
    "Y": 34,
    "Z": 35,
}
strs_36_dict = dict((v, k) for k, v in nums_36_dict.items())

for _ in range(N):
    nums.append(sys.stdin.readline().rstrip())
K = int(sys.stdin.readline().rstrip())
nums = sorted(nums, key=len, reverse=True)


sum_nums = 0
len_num = 50
change_dict = defaultdict(int)
while len_num > 0:
    for idx in range(len(nums)):
        if len(nums[idx]) == len_num:
            sum_nums += nums_36_dict[nums[idx][0]] * (36 ** (len_num - 1))
            change_dict[nums[idx][0]] += (35 - nums_36_dict[nums[idx][0]]) * (
                36 ** (len_num - 1)
            )
            if len_num != 1:
                nums[idx] = nums[idx][1:]
            else:
                nums[idx] = ""
        else:
            break
    len_num -= 1


sorted_change_dict = sorted(change_dict.items(), key=lambda item: item[1], reverse=True)
while K > 0 and sorted_change_dict:
    change = sorted_change_dict.pop(0)
    sum_nums += change[1]
    K -= 1


result = ""
while sum_nums:
    share, remain = divmod(sum_nums, 36)
    result += strs_36_dict[remain]
    sum_nums = share
result = result[::-1]
if result:
    print(result)
else:
    print(0)
