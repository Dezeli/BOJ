# 할로윈의 사탕

T = int(input())

for _ in range(T):
    c, v = map(int, input().split())

    a, b = divmod(c, v)

    print(f"You get {a} piece(s) and your dad gets {b} piece(s).")
