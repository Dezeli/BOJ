# 사나운 개

A, B, C, D = map(int, input().split())
delivery = list(map(int, input().split()))

for i in delivery:
    dogs = 0
    if 0 < i % (A + B) <= A:
        dogs += 1
    if 0 < i % (C + D) <= C:
        dogs += 1
    print(dogs)
