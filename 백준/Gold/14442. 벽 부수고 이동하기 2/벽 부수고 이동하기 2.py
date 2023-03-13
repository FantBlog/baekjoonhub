from collections import deque
dd = (
   (1,0),
   (-1,0),
   (0,1),
   (0,-1) 
)

def BFS(r,c,wall):
    for dr, dc in dd:
        if not(0 <= r + dr < R and 0 <= c + dc < C):
            continue

        if r+dr == R-1 and c + dc == C-1:
            return True
        
        if wall < K and not vis[wall+1][r+dr][c+dc] and world[r + dr][c + dc]:
            que.append((r+dr,c+dc,wall+1))
            vis[wall+1][r+dr][c+dc] = 1
        if not vis[wall][r+dr][c+dc] and not world[r + dr][c + dc]:
            que.append((r+dr,c+dc,wall))
            vis[wall][r+dr][c+dc] = 1


R, C, K = map(int,input().split())
world = [list(map(int,input())) for _ in range(R)]
vis = [[[0] * (C) for _ in range(R)] for _ in range(K+1)]
if R == 1 and C == 1:
    print(1)
    exit()
    
que = deque()

que.append((0,0,0))
vis[0][0][0] = 1
leng = 1
while que:
    leng += 1
    # print(que)
    for _ in range(len(que)):
        if BFS(*que.popleft()):
            print(leng)
            que.clear()
            exit()
print(-1)