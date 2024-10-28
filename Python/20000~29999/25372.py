# 성택이의 은밀한 비밀번호

N = int(input())
for _ in range(N):
    password = input()
    if 6 <= len(password) <= 9:
        print("yes")
    else:
        print("no")
