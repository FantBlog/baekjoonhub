N = int(input())
dp = [0] * 31
dp[0] = 1
dp[1] = 0
dp[2] = 3
for i in range(3, 31):
    if i % 2: continue
    dp[i] = dp[i-2] * 3
    for j in range(i-4,-1,-2):
        dp[i] += dp[j] * 2
print(dp[N])