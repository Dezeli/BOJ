# 계단 오르기
import sys

N = int(sys.stdin.readline().rstrip())

stream = [0, 0]
no_stream = [0, 0]

for i in range(N):
    stair = int(sys.stdin.readline().rstrip())
    no_stream.append(max([no_stream[i], stream[i]])+stair)
    stream.append(no_stream[i+1]+stair)
    
print(max(stream[-1], no_stream[-1]))