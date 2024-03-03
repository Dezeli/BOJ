# 제로

K = int(input())
queue = []
for _ in range(K):
    n = int(input())
    if n == 0:
        queue.pop()
    else:
        queue.append(n)
print(sum(queue))
