# 뉴턴과 사과

people = list(map(int, input().split()))

x, y, r = map(int, input().split())

if x in people:
    num = people.index(x) + 1
else:
    num = 0
print(num)
