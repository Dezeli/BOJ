# Another Cow Number Game

N = int(input())

score = 0
while N!=1:
    if N%2==1:
        N = N*3+1
    else:
        N = N//2
    score += 1
print(score)