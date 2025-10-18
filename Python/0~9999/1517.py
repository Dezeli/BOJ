# 버블 소트
import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))


count = 0

def merge(left, right):
    global count
    i = 0
    j = 0
    merged_list = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged_list.append(left[i])
            i += 1
        else:
            merged_list.append(right[j])
            j += 1
            count += len(left)-i
    merged_list.extend(left[i:])
    merged_list.extend(right[j:])
    return merged_list

def make_tree(s, e, i):
    if s==e:
        return [A[s]]

    mid = (s+e)//2
    left = make_tree(s, mid, i*2)
    right = make_tree(mid+1, e, i*2+1)
    merged_list = merge(left, right)
    return merged_list

make_tree(0, N-1, 1)

print(count)