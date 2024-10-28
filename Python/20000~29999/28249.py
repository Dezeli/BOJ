# Chili Peppers

N = int(input())

peppers = {
    "Poblano": 1500,
    "Mirasol": 6000,
    "Serrano": 15500,
    "Cayenne": 40000,
    "Thai": 75000,
    "Habanero": 125000,
}

price = 0
for _ in range(N):
    price += peppers[input()]

print(price)
