# Animal King Election


lion = 0
for _ in range(9):
    if input() == "Lion":
        lion += 1
if lion >= 5:
    print("Lion")
else:
    print("Tiger")
