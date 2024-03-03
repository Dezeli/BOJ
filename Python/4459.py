# Always Follow the Rules in Zombieland

q = int(input())
rules = []
for _ in range(q):
    rules.append(input())

r = int(input())
for _ in range(r):
    n = int(input())
    if 0 <= n - 1 < q:
        print(f"Rule {n}: {rules[n-1]}")
    else:
        print(f"Rule {n}: No such rule")
