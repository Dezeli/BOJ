# 최댓값 


max_num = -1
row = 10
col = 10

for i in range(1, 10):
    line = [0] + list(map(int, input().split()))
    for j in range(1, 10):
        if line[j]>max_num:
            max_num = line[j]
            row = i
            col = j

print(max_num)
print(row, col)