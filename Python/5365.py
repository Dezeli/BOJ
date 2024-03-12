# Decodermessage

n = int(input())
message = list(input().split())

for i in range(n):
    if i==0:
        print(message[i][0], end="")
    else:
        if len(message[i])>=last_len:
            print(message[i][last_len-1], end="")
        else:
            print('', end=" ")

    last_len = len(message[i])

