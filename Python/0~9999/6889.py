# Smile with Similes

n = int(input())
m = int(input())

ad = [input() for _ in range(n)]
no = [input() for _ in range(m)]

for i in ad:
    for j in no:
        print(f"{i} as {j}")
