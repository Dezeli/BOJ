# 가장 긴 바이토닉 부분 수열
import sys

input = sys.stdin.readline

N = int(input())
A = [*map(int, input().split())]


def get_max_inc(nums):
    up_list = [0 for _ in range(N)]
    max_inc = [0 for _ in range(N)]
    for num_idx in range(len(nums)):
        num = nums[num_idx]
        for i in range(N-1, -1, -1):
            if up_list[i]!=0 and up_list[i] < num:
                if up_list[i+1]==0:
                    up_list[i+1]=num
                else:
                    up_list[i+1] = min([num, up_list[i+1]])
                if max_inc[num_idx]==0:
                    max_inc[num_idx] = i+2
        if up_list[0] > num or up_list[0]==0:
            up_list[0] = num
        if max_inc[num_idx]==0:
            max_inc[num_idx] = 1
    return max_inc

ori = get_max_inc(A)
A.reverse()
rev = get_max_inc(A)
rev.reverse()
max_len = 0
for i in range(N):
    max_len = max([max_len, ori[i] + rev[i]])
print(max_len-1)


