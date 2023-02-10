from collections import deque
import sys
input = sys.stdin.readline

m, n, h= map(int,input().split())
box = [[] for _ in range(h)]
for i in range(h):
    for _ in range(n):
        box[i].append(list(map(int,input().split())))

serch = deque()
count = 0
for z in range(h):
    for x in range(m):
        for y in range(n):
            if box[z][y][x] == 1:
                serch.append((x,y,z))

while len(serch) > 0:
    for _ in range(len(serch)):
        x,y,z = serch.popleft()
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]
        dz = [-1,0,1]
        for i in range(4):
            if 0 <= y+dy[i] < n and 0 <= x+dx[i] < m:
                if box[z][y+dy[i]][x+dx[i]] == 0: # 안익은거면
                    box[z][y+dy[i]][x+dx[i]] = 1
                    serch.append((x+dx[i],y+dy[i],z))
        for j in range(3):
            if 0 <= z+dz[j] < h:
                if box[z+dz[j]][y][x] == 0: # 안익은거면
                    box[z+dz[j]][y][x] = 1
                    serch.append((x,y,z+dz[j]))
    if len(serch):
        count += 1
for j in range(h):
    for i in range(n):
        if 0 in box[j][i]:
            print(-1)
            exit()
print(count)