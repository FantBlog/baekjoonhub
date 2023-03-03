dr = (0,-1,-1)
dc = (-1,-1,0)
pipe_type = ((0,1),(0,1,2),(1,2))

N = int(input())
world = [list(map(int,input().split())) for _ in range(N)]

dp = [[[0,0,0] for _ in range(N)] for _ in range(N)]
dp[0][1][0] = 1

for r in range(N):
    for c in range(2,N):
        if world[r][c]:
            continue
        for i in [0,2]:
            dp[r][c][i] = sum(dp[r+dr[i]][c+dc[i]][j] for j in pipe_type[i])
        if not(world[r-1][c] or world[r][c-1]): # 둘다 벽이 아니면
            dp[r][c][1] = sum(dp[r+dr[1]][c+dc[1]][j] for j in pipe_type[1])

print(sum(dp[N-1][N-1]))