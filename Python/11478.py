# 서로 다른 부분 문자열의 개수

S = input()

words = set()

for i in range(len(S) + 1):
    for j in range(i + 1, len(S) + 1):
        words.add(S[i:j])
print(len(words))
