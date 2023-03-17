N, K = map(int,input().split())
mod = 1_000_000_000
dp = [[0]*(N+1) for _ in range(K)]

for i in range(N+1):
    dp[0][i] = 1

for k in range(1,K):
    for n in range(N+1):
        for i in range(n+1):
            dp[k][n] += dp[k-1][n-i]
            dp[k][n] %= mod

print(dp[K-1][N])