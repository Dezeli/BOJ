# Corona Virus Testing

g, p, t = map(int, input().split())

indvi = g*p
group = g + t*p

if indvi<group:
    print(1)
elif indvi>group:
    print(2)
else:
    print(0)