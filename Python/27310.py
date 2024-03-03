# :chino_shock:

emozi = input()

result = len(emozi)

for i in emozi:
    if i == ":":
        result += 1
    elif i == "_":
        result += 5

print(result)
