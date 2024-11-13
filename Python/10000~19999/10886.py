# 0 = not cute / 1 = cute

N = int(input())

vote = [input() for _ in range(N)]

if vote.count('1')>vote.count('0'):
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")