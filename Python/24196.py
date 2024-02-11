# Gömda ord

S = input()
idx = 0

word = ""

while idx < len(S):
    word += S[idx]
    idx += ord(S[idx])-64

print(word)