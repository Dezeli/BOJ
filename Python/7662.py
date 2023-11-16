# 이중 우선순위 큐
from sys import stdin
import heapq
from collections import defaultdict

T = int(stdin.readline().rstrip())

for _ in range(T):
    k = int(stdin.readline().rstrip())
    max_heap = []
    min_heap = []
    cnt_nums = 0
    min_check = defaultdict(int)
    max_check = defaultdict(int)
    for __ in range(k):
        ord, num = stdin.readline().rstrip().split()
        if ord == 'I':
            heapq.heappush(min_heap, int(num))
            heapq.heappush(max_heap, -int(num))
            cnt_nums += 1
        else:
            
            if cnt_nums>0:
                cnt_nums -= 1
                if num == '-1':
                    pop_num = heapq.heappop(min_heap)
                    while max_check[pop_num]:
                        max_check[pop_num] -= 1
                        pop_num = heapq.heappop(min_heap)
                    min_check[pop_num] += 1
                else:
                    pop_num = heapq.heappop(max_heap)
                    while min_check[-pop_num]:
                        min_check[-pop_num] -= 1
                        pop_num = heapq.heappop(max_heap)
                    max_check[-pop_num] += 1
    if cnt_nums:
        min_num = heapq.heappop(min_heap)
        while max_check[min_num]:
            max_check[min_num] -= 1
            min_num = heapq.heappop(min_heap)
        
        max_num = -heapq.heappop(max_heap)
        while min_check[max_num]:
            min_check[max_num] -= 1
            max_num = -heapq.heappop(max_heap)
        print(max_num, min_num)
    else:
        print("EMPTY")
