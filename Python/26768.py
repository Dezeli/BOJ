# H4x0r 

s = input()
change = {'a':'4', 'e':'3', 'o':'0', 'i':'1', 's':'5'}

for i in s:
    if i in change:
        print(change[i], end="")
    else:
        print(i, end="")
print()
