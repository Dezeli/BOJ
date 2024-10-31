# 部員の変遷

while True:
    n = int(input())
    if n==0:
        break

    student = list(map(int, input().split()))
    max_stu = 0
    for i in range(n-2):
        max_stu = max(max_stu, student[i]+student[i+1]+student[i+2])
    print(max_stu)