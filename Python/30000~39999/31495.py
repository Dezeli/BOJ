# 그게 무슨 코드니..

s = input()

if s[0] == '"' and s[-1] == '"' and len(s) >= 3:
    print(s[1:-1])
else:
    print("CE")
