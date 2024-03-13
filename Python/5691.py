# 평균 중앙값 문제

while True:
    A, B = map(int, input().split())

    if A==B==0:
        break

    print(min([A, B])*3-sum([A, B]))