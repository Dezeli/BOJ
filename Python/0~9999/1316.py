# 그룹 단어 체커

T = int(input())

time = 0
for i in range(T):
    word = input()
    alpList = []
    for i in range(len(word)):
        try:
            if i == 0:
                alpList.append(word[i])
                continue
            if word[i] == word[i - 1]:
                pass
            else:
                if word[i] in alpList:
                    time -= 1
                    break
                alpList.append(word[i])
        except:
            pass

    time += 1
print(time)
