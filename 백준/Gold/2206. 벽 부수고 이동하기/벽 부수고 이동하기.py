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
        
        if (r+dr,c+dc,wall) not in vis:
            if wall != 1 and world[r + dr][c + dc]: 
                que.append((r+dr,c+dc,1))
                vis.add((r+dr,c+dc,1))
            elif not world[r + dr][c + dc]:
                que.append((r+dr,c+dc,wall))
                vis.add((r+dr,c+dc,wall))


R, C = map(int,input().split())
world = [list(map(int,input())) for _ in range(R)]

if R == 1 and C == 1:
    print(1)
    exit()
    
que = deque()
vis = set()

que.append((0,0,0))
vis.add((0,0))
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