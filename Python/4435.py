# 중간계 전쟁

T = int(input())

for i in range(T):
    a, b, c, d, e, f = map(int, input().split())
    A, B, C, D, E, F, G = map(int, input().split())

    team1 = a + 2 * b + 3 * c + 3 * d + 4 * e + 10 * f
    team2 = A + 2 * B + 2 * C + 2 * D + 3 * E + 5 * F + 10 * G

    if team1 > team2:
        print("Battle " + str(i + 1) + ": Good triumphs over Evil")
    elif team1 < team2:
        print("Battle " + str(i + 1) + ": Evil eradicates all trace of Good")
    else:
        print("Battle " + str(i + 1) + ": No victor on this battle field")
