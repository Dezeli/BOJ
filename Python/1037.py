# 약수
import sys

c = int(sys.stdin.readline().rstrip())
m_list = list(map(int, sys.stdin.readline().split()))

N = min(m_list)*max(m_list)
print(N)
