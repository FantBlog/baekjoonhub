import sys
from collections import deque
def input(): return sys.stdin.readline().rstrip()

dd = [
    (0,-1),
    (0,1),
    (1,0),
    (-1,0)
]
def j(r,c):
    for dr, dc in dd:
        if not(0 <= r + dr < R and 0 <= c + dc < C):
            return True
        if world[r + dr][c + dc] == '.':
            world[r + dr][c + dc] = 'J'
            jihun.append((r+dr,c+dc))

def f(r,c):
    for dr, dc in dd:
        if 0 <= r + dr < R and 0 <= c + dc < C:
            if world[r + dr][c + dc] == '.' or world[r + dr][c + dc] == 'J':
                if not world[r + dr][c + dc] == 'F':
                    world[r + dr][c + dc] = 'F'
                    fire.append((r+dr,c+dc))

R, C = map(int,input().split())
world = [list(input()) for _ in range(R)]
jihun = deque()
fire = deque()
for r in range(R):
    for c in range(C):
        if world[r][c] == 'J':
            jihun.append((r,c))
        if world[r][c] == 'F':
            fire.append((r,c))
count = 0
while jihun:
    for _ in range(len(fire)):
        f(*fire.popleft())
        
    count += 1
    for _ in range(len(jihun)):
        if j(*jihun.popleft()):
            print(count)
            exit()

    
print('IMPOSSIBLE')