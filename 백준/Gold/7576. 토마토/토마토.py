from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int,input().split())
box = []
for _ in range(n):
    box.append(list(map(int,input().split())))

serch = deque()
count = 0
for x in range(m):
    for y in range(n):
        if box[y][x] == 1:
            serch.append((x,y))

while len(serch) > 0:
    for _ in range(len(serch)):
        x,y = serch.popleft()
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]
        for i in range(4):
            if 0 <= y+dy[i] < n and 0 <= x+dx[i] < m:
                if box[y+dy[i]][x+dx[i]] == 0: # 안익은거면
                    box[y+dy[i]][x+dx[i]] = 1
                    serch.append((x+dx[i],y+dy[i]))
    if len(serch):
        count += 1

for i in range(n):
    if 0 in box[i]:
        print(-1)
        exit()
print(count)