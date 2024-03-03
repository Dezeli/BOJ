# アイスクリーム (Ice Cream)

S = int(input())
A = int(input())
B = int(input())

cost = 250
h = A

while h < S:
    cost += 100
    h += B
print(cost)
