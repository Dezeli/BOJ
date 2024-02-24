# 감마선을 맞은 컴퓨터

ans = ''

for _ in range(15):
    s = input()
    for i in s:
        if i == 'w':
            ans = 'chunbae'
        elif i == 'b':
            ans = 'nabi'
        elif i == 'g':
            ans = 'yeongcheol'

print(ans)