N, K = map(int,input().split())
coins = sorted(list(int(input()) for _ in range(N)))
dp = [0] * (K+1)
for coin in coins:
    if coin <= K:
        dp[coin] += 1
    for i in range(1,K+1):
        dp[i] += dp[i-coin] if i - coin > 0 else 0
print(dp[K])