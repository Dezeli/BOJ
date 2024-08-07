# Roll the Dice

m = int(input())
n = int(input())

cnt = 0
for i in range(1, m + 1):
    if 10 - i <= n and 10 - i > 0:
        cnt += 1

if cnt == 1:
    print("There is 1 way to get the sum 10.")
else:
    print(f"There are {cnt} ways to get the sum 10.")
