# 경고

h1, m1, s1 = map(int, input().split(":"))
h2, m2, s2 = map(int, input().split(":"))


if s2 - s1 < 0:
    s = s2 - s1 + 60
    b = -1
else:
    s = s2 - s1
    b = 0

if m2 - m1 + b < 0:
    m = m2 - m1 + b + 60
    b = -1
else:
    m = m2 - m1 + b
    b = 0

if h2 - h1 + b < 0:
    h = h2 - h1 + b + 24
else:
    h = h2 - h1 + b

if h == 0 and m == 0 and s == 0:
    h = 24

print("%02d:%02d:%02d" % (h, m, s))
