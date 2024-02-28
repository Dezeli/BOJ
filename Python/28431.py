# 양말 짝 맞추기
from collections import defaultdict

socks = defaultdict(int)

for _ in range(5):
    sock_num = int(input())
    socks[sock_num] += 1

for i in range(10):
    if socks[i]%2==1:
        print(i)
        break