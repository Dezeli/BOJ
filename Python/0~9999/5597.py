# 과제 안 내신 분..?

students = [0 for _ in range(31)]
students[0] = 1
for _ in range(28):
    n = int(input())
    students[n] = 1

for i in enumerate(students):
    if i[1] == 0:
        print(i[0])
