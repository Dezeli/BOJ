# 체스 초보 브실이

score = 0
chess = {
    ".": 0,
    "K": 0,
    "k": 0,
    "P": 1,
    "p": -1,
    "N": 3,
    "n": -3,
    "B": 3,
    "b": -3,
    "R": 5,
    "r": -5,
    "Q": 9,
    "q": -9,
}


for _ in range(8):
    line = input()
    for i in line:
        score += chess[i]

print(score)
