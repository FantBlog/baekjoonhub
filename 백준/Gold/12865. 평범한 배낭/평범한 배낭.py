N,K = map(int,input().split())  # 물품수, 최대무게

dp = [[0 for _ in range(N)] for _ in range(K+1)]
# 같은 무게라면 더 높은 가치
item = []
for _ in range(N):
    w, v  = map(int,input().split())
    item.append((w,v)) # 무게, 가치

item.sort(key=lambda x:x[0],reverse=True)


for n in range(N):
    w,v = item[n]
    for i in range(K+1):
        if i >= w:
            if n >= 1: # 전수, 더하기, 지금 값
                dp[i][n] = max(dp[i-1][n], dp[i][n-1] , dp[i-w][n-1] + v)
            else:
                dp[i][n] = max(dp[i-1][n], v)

print(max(dp[K]))