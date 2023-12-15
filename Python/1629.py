# 곱셈
import sys

A, B, C = map(int, sys.stdin.readline().split(" "))

def multi (A, B):
  if B == 1:
      return A%C
  else:
      temp = multi(A, B//2)
      if B%2 ==0:
          return (temp * temp) % C
      else:
          return (temp  * temp * A) % C
          
print(multi(A, B))