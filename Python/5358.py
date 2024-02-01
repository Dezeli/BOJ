# Football Team

while True:
    try:
        name = input()
        for s in name:
            if s=='i':
                s = 'e'
            elif s=='e':
                s = 'i'
            elif s=='I':
                s = 'E'
            elif s=='E':
                s = 'I'
            print(s, end="")
        print()
    except:
        break