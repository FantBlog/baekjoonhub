N, K = map(int,input().split())
coin = [int(input()) for _ in range(N)]
dp = [float('inf') for _ in range(K+1)]
dp[0] = 0

for i in coin:
    for j in range(i,K+1):
        dp[j] = min(dp[j], dp[j-i]+1)
        
if dp[K] == float('inf'):
    print(-1)
else:
    print(dp[K])