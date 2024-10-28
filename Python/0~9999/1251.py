# 단어 나누기

s = input()
words = []

for i in range(1, len(s)):
    for j in range(i + 1, len(s)):
        first = s[:i][::-1]
        second = s[i:j][::-1]
        third = s[j:][::-1]
        words.append(first + second + third)

words.sort()
print(words[0])
