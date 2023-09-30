# OKUPLJANJE 
import sys

L, P = map(int, sys.stdin.readline().split(" "))
Participants = list(map(int, sys.stdin.readline().split(" ")))
for i in Participants:
    print(i - (L * P), end=" ")
