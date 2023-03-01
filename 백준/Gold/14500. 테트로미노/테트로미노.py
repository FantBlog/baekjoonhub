import sys
from collections import deque
def input(): return sys.stdin.readline().rstrip()

dd = (
    (0,1),
    (0,-1),
    (1,0),
    (-1,0)
)
def nemo(r,c):
    global mx
    total = tetris[r][c] + tetris[r+1][c] + tetris[r][c+1] + tetris[r+1][c+1]
    if total > mx:
        mx = total

def bol(r,c):
    global mx
    total = []
    for dr, dc in dd:
        if not(0 <= r + dr < R and 0 <= c + dc < C):
            continue
        total.append(tetris[r+dr][c+dc])

    if len(total) == 4:
        if mx < sum(total) - min(total) + tetris[r][c]:
            mx = sum(total) - min(total) + tetris[r][c]

    elif len(total) == 3:
        if mx < sum(total) + tetris[r][c]:
            mx = sum(total) + tetris[r][c]

def bfs(r,c):
    for dr, dc in dd:
        if not(0 <= r + dr < R and 0 <= c + dc < C):
            continue
        if (r+dr,c+dc) not in vis:
            que.append((r+dr,c+dc))
            vis[(r+dr,c+dc)] = i
            vis_data[(r+dr,c+dc)] = vis_data[(r,c)] + tetris[r+dr][c+dc]
        elif vis[(r+dr,c+dc)] == i:
            vis_data[(r+dr,c+dc)] = max(vis_data[(r+dr,c+dc)], vis_data[(r,c)] + tetris[r+dr][c+dc])

# for _ in range(19):
R, C = map(int,input().split())
tetris = [list(map(int,input().split())) for _ in range(R)]
mx = 0
que = deque()
vis = dict()
vis_data = dict()
for r in range(R):
    for c in range(C):
        if 0 <= r < R-1 and 0 <= c < C-1:
            nemo(r,c)
        bol(r,c)
        vis_data[(r,c)] = tetris[r][c]
        vis[(r,c)] = 0
        que.append((r,c))

        for i in range(1,4):
            for _ in range(len(que)):
                bfs(*que.popleft())

        if mx < max(vis_data.values()):
            mx = max(vis_data.values())

        que.clear()
        vis_data.clear()
        vis.clear()
print(mx)