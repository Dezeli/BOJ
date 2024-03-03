# FILIP

A, B = input().split(" ")
reverseA = A[::-1]
reverseB = B[::-1]

if reverseA > reverseB:
    print(reverseA)
else:
    print(reverseB)
