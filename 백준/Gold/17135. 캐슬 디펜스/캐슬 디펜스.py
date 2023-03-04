import copy
import sys
from collections import deque
def input(): return sys.stdin.readline().rstrip()

def BFS(can,cattle,r,c):
    dd = (
        (0,-1),
        (-1,0),
        (0,1)
    )

    for dr,dc in dd:
        if not(0 <= r + dr < R and 0 <= c + dc < C):
            continue

        if cattle[r+dr][c+dc]:
            can.append((r+dr, c+dc))
        
        if (r+dr,c+dc) not in vis:
            que.append((r+dr,c+dc))
            vis.add((r+dr,c+dc))
    
    return can


def archer(arr):
    result = 0 # 잡은 적 수
    ene = [()] * 3
    cattle = copy.deepcopy(world) # 성 복사
        
    for _ in range(raw): # 최고 적 높이
        for i in range(3):
            can = [(-1,-1)]
            que.clear() # 초기화
            vis.clear()
            que.append((R,arr[i])) # 시작점
            vis.add((R,arr[i]))
            
            d = 1 # 사격 사거리

            while que: # BFS
                if d > D: # 사거리 밖이면
                    break
                
                for _ in range(len(que)):
                    can = BFS(can,cattle,*que.popleft())

                d += 1 # 사격 사거리

                vis.clear()
                if len(can) > 1:
                    break
            
            can.sort(key=lambda x:(x[1],x[0]))
            if len(can) > 1:
                ene[i] = can[1]
            else:
                ene[i] = can[0]

        for r, c in ene:
            if r != -1 and c != -1 and cattle[r][c]:
                cattle[r][c] = 0
                result += 1
        
        ene = [()] * 3

        cattle = [[0]*C] + cattle[:-1]

    return result


R, C, D = map(int,input().split())
world = [0] * R
raw = 0
for r in range(R):
    world[r] = list(map(int,input().split()))
    if not raw and world[r].count(1):
        raw = R - r

mx = 0
que = deque()
vis = set()

for one in range(C-2):
    for two in range(one+1,C-1):
        for three in range(two+1,C):
            now = archer([one,two,three])
            if mx < now:
                mx = now
print(mx)