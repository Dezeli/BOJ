# 좋은 암호
import sys

K, L = map(int, sys.stdin.readline().split())

password = True
for i in range(2, L):
    if K % i == 0:
        password = False
        break
if password:
    print("GOOD")
else:
    print(f"BAD {i}")
