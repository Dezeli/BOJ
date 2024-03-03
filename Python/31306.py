# Is Y a Vowel?

s = input()

vowel = 0
assume = 0

vowels = ["a", "e", "i", "o", "u"]

for i in s:
    if i in vowels:
        vowel += 1
        assume += 1
    if i == "y":
        assume += 1

print(vowel, assume)
