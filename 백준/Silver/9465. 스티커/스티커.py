t = int(input())
for tc in range(1,t+1):
    N = int(input())
    stic = [list(map(int,input().split())) for _ in range(2)]
    dp = [[0]*N for _ in range(2)]
    dp[0][0] = stic[0][0]
    dp[1][0] = stic[1][0]
    
    for i in range(1,N):
        for j in range(2):
            dp[j][i] = max(dp[j][i-1],dp[j-1][i-1]+stic[j][i])
    
    result = max(dp[0][N-1],dp[1][N-1])
    print(result)