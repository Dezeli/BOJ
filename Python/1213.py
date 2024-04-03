# 팰린드롬 만들기


S = input()
alp = [0 for _ in range(26)]

for i in S:
    alp[ord(i)-65] += 1

pd = []
cnt = 0
mid = ''
for i in range(26):
    if alp[i]%2==1:
        cnt += 1
        mid = chr(i+65)
    for _ in range(alp[i]//2):
        pd.append(chr(i+65))
rev_pd = ''.join(pd[::-1])

if cnt>=2:
    print("I'm Sorry Hansoo")
else:
    print(''.join(pd)+mid+rev_pd)