# Judging Olympia

while True:
    scores = sorted(list(map(int, input().split())))
    if sum(scores) == 0:
        break
    scores = scores[1:-1]
    avg = sum(scores)/4
    print(avg if sum(scores)%4 else int(avg))