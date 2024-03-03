# Self Numbers

nums = [i for i in range(1, 10001)]


def checkSelfNumber(num):
    numStr = str(num)
    strSum = 0
    for i in numStr:
        strSum += int(i)
    try:
        nums.remove(strSum + num)
    except:
        pass


for i in range(10000):
    checkSelfNumber(i)
for i in nums:
    print(i)
