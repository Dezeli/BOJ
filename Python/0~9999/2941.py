# LJESNJAK

word = input()
length = 0
newAlpList = ["=", "-", "j"]
for i in range(len(word)):
    if word[i] in newAlpList:
        length -= 1
        try:
            if word[i] == "=" and word[i - 2] == "d" and word[i - 1] == "z":
                length -= 1
        except:
            pass
        try:
            if word[i] == "j":
                if word[i - 1] == "l" or word[i - 1] == "n":
                    pass
                else:
                    length += 1
        except:
            pass
    length += 1
print(length)
