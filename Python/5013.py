# Death Knight Hero

n = int(input())

win = 0
for _ in range(n):
    s = input()
    result = s.find('CD')
    if result==-1:
        win += 1
print(win)

