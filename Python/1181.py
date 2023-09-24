# 단어 정렬

N = int(input())

wordList = []
for i in range(51):
    wordList.append([])
for i in range(N):
    word = input()
    if word not in wordList[len(word)]:
        wordList[len(word)].append(word)
for i in range(51):
    wordList[i].sort()
    for j in wordList[i]:
        print(j)
        