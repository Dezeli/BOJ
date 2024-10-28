# X 보다 작은 수

N, X = list(map(int, input().split(" ")))
A = input().split(" ")
A = list(map(int, A))

for i in A:
    if i < X:
        print(i, end=(" "))
