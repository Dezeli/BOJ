# 도미노 

N = int(input())
eyes = 0
for i in range(1, N+1):
    eyes += 1.5 * i * (i+1)

print(int(eyes))