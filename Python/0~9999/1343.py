# 폴리오미노

X = list(input().split("."))

s = []
for i in X:
    if len(i) % 2 != 0:
        s = ["-1"]
        break

    if len(i) == 0:
        s.append("")
    elif len(i) % 4 == 0:
        s.append("A" * len(i))
    else:
        a = len(i) // 4
        s.append("A" * (a * 4) + "B" * 2)
print(".".join(s))
