# 뒤집기

S = input()

last = S[0]
cnt1 = 0
cnt0 = 0

if last=='1':
    cnt1 += 1
else:
    cnt0 += 1
for i in S:
    if last!=i:
        if i=='1':
            cnt1 += 1
        else:
            cnt0 += 1
    last = i

print(min(cnt1, cnt0))

