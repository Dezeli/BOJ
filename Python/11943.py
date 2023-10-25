# 파일 옮기기
import sys

A, B = map(int, sys.stdin.readline().split())
C, D = map(int, sys.stdin.readline().split())
print(min([A + D, C + B]))
