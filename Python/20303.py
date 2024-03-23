# 할로윈의 양아치
import sys  
input = sys.stdin.readline  


N, M, K = map(int, input().split())  
candies = [0] + [*map(int, input().split())]  
group = [i for i in range(N+1)]  
cnt_f = [1] * (N+1)  

def union(x, y):  
    x = find(x)  
    y = find(y)  
    if x < y:  
        x, y = y, x  
    group[x] = y  

def find(n):  
    if group[n] != n:  
        group[n] = find(group[n])  
    return group[n]  

def rob():  
    for i in range(1, N+1):  
        if i != group[i]:  
            continue  
        for j in range(K-1, cnt_f[i]-1, -1):  
            dp[j] = max(dp[j], dp[j-cnt_f[i]] + candies[i])  


for i in range(M):  
    a, b = map(int, input().split())  
    union(a, b)  

for i in range(1, N+1):  
    if i != group[i]:  
        friend = find(i)  
        candies[friend] += candies[i]  
        cnt_f[friend] += cnt_f[i]  

dp = [0 for _ in range(K)]  
rob()  
print(max(dp))