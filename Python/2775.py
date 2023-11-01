# 부녀회장이 될테야

T = int(input())

save_dict = {}

def find_people(a, b):
    if a==0:
        return b
    if b==1:
        return 1
    if (a, b) in save_dict.keys():
        return save_dict[(a, b)]
    
    people = find_people(a-1, b) + find_people(a, b-1)
    save_dict[(a, b)] = people
    return people

for _ in range(T):
    k = int(input())
    n = int(input())
    print(find_people(k, n))
