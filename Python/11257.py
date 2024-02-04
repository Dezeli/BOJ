# IT Passport Examination

n = int(input())

for _ in range(n):
    name, S, M, T = map(int, input().split())

    if S+M+T>=55 and S>=35*0.3 and M>=25*0.3 and T>=40*0.3:
        print(f"{name} {S+M+T} PASS")
    else:
        print(f"{name} {S+M+T} FAIL")