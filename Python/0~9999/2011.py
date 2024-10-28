# 암호코드

code = [0] + list(map(int, input()))
l = len(code) - 1
dp = [0 for _ in range(5000 + 1)]
if code[1] == 0:
    print(0)
else:
    dp[0] = dp[1] = 1
    for i in range(2, l + 1):
        if code[i] > 0:
            dp[i] += dp[i - 1]
        case = code[i - 1] * 10 + code[i]
        if case >= 10 and case <= 26:
            dp[i] += dp[i - 2]
    print(dp[l] % 1000000)
