# When Do We Finish?

while True:
    s, d = input().split()
    if s==d=='00:00':
        break
    sH, sM = map(int, s.split(':'))
    dH, dM = map(int, d.split(':'))
    fH, fM = sH+dH, sM+dM
    fH += fM//60
    fM %= 60
    day = fH//24
    fH %= 24

    fH = format(fH, '02')
    fM = format(fM, '02')

    if day:
        print(f"{fH}:{fM} +{day}")
    else:
        print(f"{fH}:{fM}")