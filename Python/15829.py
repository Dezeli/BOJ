# Hashing
L = int(input())
string = input()
val = 0
for i in range(L):
    val += (ord(string[i]) - 96) * (31**i)
print(val % 1234567891)
