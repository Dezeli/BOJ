# 세 막대

line = sorted(list(map(int, input().split())))

if line[0] + line[1] > line[2]:
    print(sum(line))
else:
    print((line[0]+line[1])*2-1)

