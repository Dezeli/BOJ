# 비밀번호 찾기
import sys

N, M = map(int, sys.stdin.readline().split(" "))
pw_dict = {}

for _ in range(N):
    site, pw = sys.stdin.readline().rstrip().split(" ")
    pw_dict[site] = pw

for _ in range(M):
    site = sys.stdin.readline().rstrip()
    print(pw_dict[site])
