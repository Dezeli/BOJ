# The Embarrassed Cryptographe
import sys

P, K = map(int, sys.stdin.readline().split())

password = True
for i in range(2, K):
    if P % i == 0:
        password = False
        break
if password:
    print("GOOD")
else:
    print(f"BAD {i}")
