# 출석 이벤트

N = int(input())
P = int(input())

min_cost = [P]

if N>=5:
    min_cost.append(max(P-500, 0))
if N>=10:
    min_cost.append(max(P*9//10, 0))
if N>=15:
    min_cost.append(max(P-2000, 0))
if N>=20:
    min_cost.append(max(P*3//4, 0))

print(min(min_cost))