# Счастье Мистера Бина

n = int(input())
a = map(int, input().split())

result = 0
for i in a:
    if i % 2 == 1:
        result -= 1
    else:
        result += 1
if result > 0:
    print("Happy")
else:
    print("Sad")
