import sys
from collections import deque
def input(): return sys.stdin.readline().rstrip()

def bfs(r,c):
    dd = (
        (-1,0),
        (0,-1),
        (0,1),
        (1,0)
    )

    for dr, dc in dd:
        if not(0 <= r + dr < N and 0 <= c + dc < N):
            continue
        if (r+dr,c+dc) not in vis and (sea[r+dr][c+dc] == size or sea[r+dr][c+dc] == 0): # 지나만 갈수 있음
            que.append((r+dr,c+dc))
            vis.add((r+dr,c+dc))

        elif (r+dr,c+dc) not in vis and 0 < sea[r+dr][c+dc] < size: # 먹을수 있음
            foods.append((r+dr,c+dc))
    
    return False

N = int(input())
sea = [list(map(int,input().split())) for _ in range(N)]
size = 2
eat = 0

que = deque()
vis = set()
foods = []

for i in range(N*N):
    r,c = divmod(i,N)
    if sea[r][c] == 9:
        start = (r,c)
        que.append(start)
        vis.add(start)
        break

now_time = 0
total_time = 0
while que:
    now_time += 1
    for _ in range(len(que)):
        bfs(*que.popleft())
    if foods:
        result = sorted(foods,key=lambda x : (x[0],x[1]))[0]
        total_time += now_time
        now_time = 0

        sea[start[0]][start[1]] = 0
        sea[result[0]][result[1]] = 9

        eat += 1
        if size == eat:
            size += 1
            eat = 0
        
        start = result
        que.clear()
        que.append(start)
        vis.clear()
        vis.add(start)
        foods = []
print(total_time)