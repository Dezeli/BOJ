# Juta teekond


pos = [[1, 6, 2], [1, 6, 5], [1, 8, 5], [1, 8, 2], [3, 6, 2], [3, 8, 2], [3, 6, 5], [3, 8, 5]]

memo = [int(input()) for i in range(3)]
if memo in pos:
    print("JAH")
else:
    print("EI")
