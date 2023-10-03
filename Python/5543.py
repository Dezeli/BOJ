# 상근날드

burgerList = []
drinkList = []
for i in range(3):
    burgerList.append(int(input()))
for i in range(2):
    drinkList.append(int(input()))
burgerList.sort()
drinkList.sort()
print(burgerList[0] + drinkList[0] - 50)
