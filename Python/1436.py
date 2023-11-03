# 영화감독 숌
import sys

N = int(sys.stdin.readline().rstrip())

title = 665
num = 0
while num!=N:
    title += 1
    if str(title).count('666')>=1:
        num += 1
    
print(title)