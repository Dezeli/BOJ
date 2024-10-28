# Zagubiona litera
import string

S = input()

for i in list(string.ascii_uppercase):
    if i not in S:
        print(i)
