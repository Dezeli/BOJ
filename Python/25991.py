# Lots of Liquid

n = int(input())
boxes = [i**3 for i in list(map(float, input().split()))]
result = sum(boxes) ** (1 / 3)
print(result)
