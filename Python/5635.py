# 생일

people = []

n = int(input())
for _ in range(n):
    name, d, m, y = input().split()
    d = int(d)
    m = int(m)
    y = int(y)
    people.append([y, m, d, name])
people.sort()
print(people[-1][3])
print(people[0][3])