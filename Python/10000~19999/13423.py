# Three Dots
import sys
import itertools

input = sys.stdin.readline

def search(s, e, i):
    while s <= e:
        mid = (s+e)//2
        if dots[mid] == i:
            return True
        elif dots[mid] > i : 
            e = mid - 1
        else:
            s = mid + 1

    return False
T = int(input())
for _ in range(T):
    N = int(input())
    dots = list(map(int, input().split()))
    dots.sort()
    
    cnt = 0
    for i in range(N-1):
        for j in range(i+1, N):
            l = 2*dots[j] - dots[i]
            if search(j+1, N-1, l): 
                cnt += 1

    print(cnt)