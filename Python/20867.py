# Rulltrappa

M, S, G = map(int, input().split())
A, B = map(float, input().split())
L, R = map(int, input().split())

lwait = L / A
rwait = R / B

lv = M / G + 1 if M % G else M / G
rv = M / S + 1 if M % S else M / S

if lv + lwait < rv + rwait:
    print("friskus")
else:
    print("latmask")
