# 완전 세제곱

for a in range(2, 101):
    for b in range(2, 101):
        for c in range(b + 1, 101):
            for d in range(c + 1, 101):
                if a * a * a == (b * b * b + c * c * c + d * d * d):
                    print(f"Cube = {a}, Triple = ({b},{c},{d})")
                elif a * a * a < (b * b * b + c * c * c + d * d * d):
                    break
