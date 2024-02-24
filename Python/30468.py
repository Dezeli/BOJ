# 호반우가 학교에 지각한 이유 1

STR, DEX, INT, LUK, N = map(int, input().split())

if sum([STR, DEX, INT, LUK])>=N*4:
    print(0)
else:
    print(N*4-sum([STR, DEX, INT, LUK]))