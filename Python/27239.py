# Шахматная доска

n = int(input())

num, alp = divmod(n, 8)

if alp==0:
    alp = 8
    num -= 1

print(f"{chr(alp+96)}{num+1}")