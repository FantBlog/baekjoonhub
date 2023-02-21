import sys
from collections import deque
def input(): return sys.stdin.readline().rstrip()

dd = [
    (-1,-1),
    (-1,0),
    (-1,1),
    (0,-1),
    (0,1),
    (1,-1),
    (1,0),
    (1,1)
]

N, M, K = map(int,input().split()) # 지도크기, 나무개수, 년도
S2D2 = [list(map(int,input().split())) for _ in range(N)] # 로봇
tree = [[deque() for _ in range(N)] for _ in range(N)] # 나무정보 c,r,나이
for _ in range(M):
    r, c, y = map(int,input().split())
    tree[r-1][c-1].append(y)
garden = [[5]*N for _ in range(N)] # 양분 기본 5
grow = [[0]*N for _ in range(N)]
death =[[deque() for _ in range(N)] for _ in range(N)]

for k in range(K): 
    for r in range(N):
        for c in range(N):
            for _ in range(len(tree[r][c])):
                year = tree[r][c].popleft()
                if garden[r][c] >= year: # 양분 되면
                    garden[r][c] -= year
                    year += 1
                    tree[r][c].append(year)
                    if year % 5 == 0:
                        grow[r][c] += 1
                else:
                    death[r][c].append(year)
                    
    for r in range(N):
        for c in range(N):
            while death[r][c]:
                garden[r][c] += death[r][c].pop() // 2

            while grow[r][c]: # 자라난 나무수만큼
                for dr, dc in dd:
                    if 0 <= c+dc < N and 0 <= r+dr < N: # 상도의 땅 벗어나는경우
                        tree[r+dr][c+dc].appendleft(1) # 나이 1인 나무 심기
                grow[r][c] -= 1
                
            garden[r][c] += S2D2[r][c]

total = 0
for r in range(N):
    for c in range(N):
        total += len(tree[r][c])
print(total)