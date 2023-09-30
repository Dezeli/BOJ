# ŠEĆER 

N = int(input())

fiveBagNum = N // 5
fiveBag = 0
threeBag = 0
for i in range(fiveBagNum):
    if (N - (fiveBagNum - i) * 5) % 3 == 0:
        fiveBag = fiveBagNum - i
        threeBag = (N - (fiveBagNum - i) * 5) // 3
        print(fiveBag + threeBag)
        break
if fiveBag == 0:
    if N % 3 == 0:
        print(N // 3)
    else:
        print("-1")
