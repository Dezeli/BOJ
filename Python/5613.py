# 계산기 프로그램

result = int(input())
while True:
    s = input()
    if s == "=":
        print(result)
        break

    if s == "+":
        s = int(input())
        result += s
    if s == "-":
        s = int(input())
        result -= s
    if s == "*":
        s = int(input())
        result *= s
    if s == "/":
        s = int(input())
        result //= s
