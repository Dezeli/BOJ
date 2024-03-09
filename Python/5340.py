# Secret Location

cnt = []

for _ in range(6):
    s = input().rstrip()
    cnt.append(len(s))

print(f"Latitude {cnt[0]}:{cnt[1]}:{cnt[2]}")
print(f"Longitude {cnt[3]}:{cnt[4]}:{cnt[5]}")