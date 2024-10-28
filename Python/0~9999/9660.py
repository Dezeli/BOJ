# 돌 게임 6

N = int(input())

score = [False, True, False, True, True, True, True]

if score[N % 7]:
    print("SK")
else:
    print("CY")
