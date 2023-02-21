import sys
from collections import deque
def input(): return sys.stdin.readline().rstrip()

dd = [
    (0,-1),
    (0,1),
    (1,0),
    (-1,0)
]

def findr(r,c):
    for dr, dc in dd:
        if 0 <= r + dr < N and 0 <= c + dc < N and check[r + dr][c + dc] and paper[r+dr][c+dc] == 'R':
            check[r + dr][c + dc] = False
            que.append((r+dr,c+dc))

def findg(r,c):
    for dr, dc in dd:
        if 0 <= r + dr < N and 0 <= c + dc < N and check[r + dr][c + dc] and paper[r+dr][c+dc] == 'G':
            check[r + dr][c + dc] = False
            que.append((r+dr,c+dc))

def findb(r,c):
    for dr, dc in dd:
        if 0 <= r + dr < N and 0 <= c + dc < N and check[r + dr][c + dc] and paper[r+dr][c+dc] == 'B':
            check[r + dr][c + dc] = False
            que.append((r+dr,c+dc))

def findrg(r,c):
    for dr, dc in dd:
        if 0 <= r + dr < N and 0 <= c + dc < N and check[r + dr][c + dc]:
            if paper[r+dr][c+dc] == 'G' or paper[r+dr][c+dc] == 'R':
                check[r + dr][c + dc] = False
                que.append((r+dr,c+dc))

N = int(input())
paper = [list(input()) for _ in range(N)]


check = [[True]*N for _ in range(N)] # 안간게 트루
que = deque()
count = 0
count2 = 0

for dvmd in range(N*N):
    r, c = divmod(dvmd,N)
    if check[r][c]:
        count += 1
        if paper[r][c] == 'R':
            check[r][c] = False
            que.append((r,c))
            while que:
                findr(*que.popleft())
        if paper[r][c] == 'G':
            check[r][c] = False
            que.append((r,c))
            while que:
                findg(*que.popleft())
        if paper[r][c] == 'B':
            check[r][c] = False
            que.append((r,c))
            while que:
                findb(*que.popleft())

check = [[True]*N for _ in range(N)] # 안간게 트루
que = deque()

for dvmd in range(N*N):
    r, c = divmod(dvmd,N)
    if check[r][c]:
        count2 += 1
        if paper[r][c] == 'R' or paper[r][c] == 'G':
            check[r][c] = False
            que.append((r,c))
            while que:
                findrg(*que.popleft())
        if paper[r][c] == 'B':
            check[r][c] = False
            que.append((r,c))
            while que:
                findb(*que.popleft())

print(count, count2)