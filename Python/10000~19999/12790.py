# Mini Fantasy War

T = int(input())

for _ in range(T):
    HP1, MP1, A1, D1, HP2, MP2, A2, D2 = map(int, input().split())
    HP = max(HP1 + HP2, 1)
    MP = max(MP1 + MP2, 1)
    A = max(A1 + A2, 0)
    D = D1 + D2
    print(HP+5*MP+2*A+2*D)
