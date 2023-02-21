N = int(input())
color = [list(map(int,input().split())) for _ in range(N)]
dp = [[0] * 3 for _ in range(N)]
for i in range(3):
    dp[0][i] = color [0][i]

for i in range(1,N):
    dp[i][0] = min([dp[i-1][j] for j in (1,2)]) + color[i][0]
    dp[i][1] = min([dp[i-1][j] for j in (0,2)]) + color[i][1]
    dp[i][2] = min([dp[i-1][j] for j in (0,1)]) + color[i][2]

print(min(dp[N-1]))