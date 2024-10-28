# Дневник Гравити Фолз

w, h = map(int, input().split())

n, a, b = map(int, input().split())

if a > w or b > h:
    print(-1)
else:
    paper, left = divmod(n, ((w // a) * (h // b)))
    if left:
        print(paper + 1)
    else:
        print(paper)
