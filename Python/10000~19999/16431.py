# 베시와 데이지

Br, Bc = map(int, input().split())
Dr, Dc = map(int, input().split())
Jr, Jc = map(int, input().split())

B = max(abs(Br-Jr), abs(Bc-Jc))
D = abs(Dr-Jr) + abs(Dc-Jc)

if B>D:
    print('daisy')
elif B<D:
    print('bessie')
else:
    print('tie')