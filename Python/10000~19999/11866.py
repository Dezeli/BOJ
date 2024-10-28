# 요세푸스 문제 0

N, K = map(int, input().split())

queue = [i for i in range(1, N + 1)]

puth = []

num = 0
while queue:
    num += 1
    pick = queue.pop(0)
    if num % K == 0:
        puth.append(pick)
    else:
        queue.append(pick)

print(f"<{puth[0]}", end="")
for i in puth[1:]:
    print(f", {i}", end="")
print(">")
