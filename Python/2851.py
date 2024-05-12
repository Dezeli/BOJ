# 슈퍼 마리오

score = 0
fin = False
for _ in range(10):
    mushroom = int(input())

    if score + mushroom <= 100:
        score += mushroom
    else:
        fin = True
        if (score + mushroom) - 100 <= 100 - score:
            print(score + mushroom)
        else:
            print(score)
        break
if not fin:
    print(score)
