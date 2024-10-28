# 세금
import sys

N = int(sys.stdin.readline().rstrip())
print(N * 78 // 100, N * 80 // 100 + N * 20 // 100 * 78 // 100)
