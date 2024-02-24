# 임스의 메이플컵

N, U, L = map(int, input().split())

if N>=1000:
    if U>=8000 or L>=260:
        print("Very Good")
    else:
        print("Good")
else:
    print("Bad")