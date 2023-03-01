import sys
from collections import deque
def input(): return sys.stdin.readline().rstrip()

dd = (
    (0,1),
    (0,-1),
    (1,0),
    (-1,0)
)
def BFS(r,c):
    for dr, dc in dd:
        if not(0 <= r + dr < R and 0 <= c + dc < C):
            continue
        if r + dr == R-1 and c + dc == C-1:
            return True
        if (r+dr,c+dc) not in vis and world[r+dr][c+dc]:
            que.append((r+dr,c+dc))
            vis.add((r+dr,c+dc))


R, C = map(int,input().split())
world = [list(map(int,input())) for _ in range(R)]

que = deque()
vis = set()
que.append((0,0))
vis.add((0,0))
leng = 1

while que:
    leng += 1
    for _ in range(len(que)):
        if BFS(*que.popleft()):
            print(leng)
            exit()