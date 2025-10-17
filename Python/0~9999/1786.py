# 찾기

T = input()
P = input()

def get_pi(P):
    m = len(P)
    pi = [0]*m
    j = 0

    for i in range(1, m):
        while j > 0 and P[i] != P[j]:
            j = pi[j - 1]

        if P[i] == P[j]:
            j += 1
            pi[i] = j

    return pi

pi = get_pi(P)

pattern = []
j = 0
for i in range(len(T)):
    while j > 0 and T[i] != P[j]:
        j = pi[j - 1]

    if T[i] == P[j]:
        j += 1
        if j == len(P):
            pattern.append(i - len(P) + 2)
            j = pi[j - 1]

print(len(pattern))
print(*pattern)