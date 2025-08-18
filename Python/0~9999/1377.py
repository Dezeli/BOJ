# 버블 소트
import sys

input = sys.stdin.readline

N = int(input())
array = []
for i in range(N):
    array.append((int(input()), i))

sorted_arr = sorted(array) 
ans = [] 

for i in range(N):
    ans.append(sorted_arr[i][1] - array[i][1])

print(max(ans) + 1)