# 소가 길을 건너간 이유 2
import sys

input = sys.stdin.readline

S = input().rstrip()

ans = 0 
for i in range(52):
    for j in range(i+1,52):
        if S[i] == S[j]:
            cows = S[i:j+1]
            for i in cows:
                if cows.count(i) == 1:                    
                    ans += 1
            break
print(ans//2)