# FBI

agent = []

for i in range(1, 6):
    s = input()
    if "FBI" in s:
        agent.append(i)

if agent:
    print(*agent)
else:
    print("HE GOT AWAY!")
