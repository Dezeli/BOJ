# Good times

ot = input()
while len(ot) != 4:
    ot = "0" + ot
print(int(ot), "in Ottawa")
h, m = ot[:2], ot[2:]

if int(h) - 3 < 0:
    print(int(str(int(h) - 3 + 24) + m), "in Victoria")
else:
    print(int(str(int(h) - 3) + m), "in Victoria")
if int(h) - 2 < 0:
    print(int(str(int(h) - 2 + 24) + m), "in Edmonton")
else:
    print(int(str(int(h) - 2) + m), "in Edmonton")
if int(h) - 1 < 0:
    print(int(str(int(h) - 1 + 24) + m), "in Winnipeg")
else:
    print(int(str(int(h) - 1) + m), "in Winnipeg")
print(int(ot), "in Toronto")
if int(h) + 1 == 24:
    print(int(m), "in Halifax")
else:
    print(int(str(int(h) + 1) + m), "in Halifax")
sm = int(m) + 30
if sm >= 60:
    sh = str(int(h) + 2)
    sm -= 60
else:
    sh = str(int(h) + 1)
if sm == 0 and sh != 0:
    sm = "00"
else:
    sm = str(sm)
if int(sh) > 23:
    sh = str(int(sh) - 24)
print(int(sh + sm), "in St. John's")
