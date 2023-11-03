# 숫자 카드 2

N = int(input())
cards = list(map(int, input().split()))

M = int(input())
check_list = list(map(int, input().split()))

cards.sort()

for check in check_list:
    start = 0
    end = len(cards) - 1
    amount = 0

    while start <= end:
        mid = (start + end) // 2
        if cards[mid] == check:
            amount += 1
            break
        elif cards[mid] > check:
            end = mid - 1
        else:
            start = mid + 1

    midplus = mid + 1
    midminus = mid - 1
    if midplus < N:
        while cards[midplus]==check:
            amount += 1
            if midplus < N-1: 
                midplus += 1
            else:
                break
    if 0 <= midminus:
        while cards[midminus]==check:
            amount += 1
            if 0 < midminus:
                midminus -= 1
            else:
                break


    print(amount, end=" ")