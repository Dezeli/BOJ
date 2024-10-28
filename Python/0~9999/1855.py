# 암호
import sys

K = int(sys.stdin.readline().rstrip())
password = sys.stdin.readline().rstrip()

real = ["" for _ in range(K)]

pattern1 = [i for i in range(K)]
pattern2 = pattern1[::-1]
pattern = (pattern1 + pattern2) * 200

for i in range(len(password)):
    real[pattern[i]] += password[i]

answer = ""
for i in real:
    answer += i

print(answer)
