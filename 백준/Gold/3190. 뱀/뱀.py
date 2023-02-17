from collections import deque
D = [[0,-1],[1,0],[0,1],[-1,0]] # 북, 동, 남, 서
dirt = 1
N = int(input()) # 보드

world = [[0]*N for _ in range(N)]
world[0][0] = 1

stack = deque()
stack.append((0,0))

time = 0

K = int(input()) # 사과수
for _ in range(K):
    r, c = map(int,input().split())
    world[r-1][c-1] = 2 # 사과

L = int(input()) # 뱀방향 수
for _ in range(L):
    move , turn = input().split()
    for _ in range(time,int(move)):

        x,y = stack[0][0]+D[dirt][0], stack[0][1]+D[dirt][1] # 머리 좌표

        stack.appendleft((x,y)) # 움직임
        time += 1

        if x < 0 or y < 0 or x >= N or y >= N or world[y][x] == 1: # 몸 or 벽
            print(time)
            exit()

        elif world[y][x] == 2: # 사과 먹으면
            pass

        else:
            dx, dy = stack.pop() # 꼬리 제거
            world[dy][dx] = 0
        
        world[y][x] = 1 # 지도에 기록


    if turn == 'D': # 우회전
        dirt += 1
    else: dirt -= 1

    if dirt > 3: # 동서남북 이어지게
        dirt = 0
    if dirt < 0:
        dirt = 3

while True:

    x,y = stack[0][0]+D[dirt][0], stack[0][1]+D[dirt][1] # 머리 좌표

    stack.appendleft((x,y)) # 움직임
    time += 1

    if x < 0 or y < 0 or x >= N or y >= N or world[y][x] == 1: # 몸 or 벽
        print(time)
        exit()

    elif world[y][x] == 2: # 사과 먹으면
        pass

    else:
        dx, dy = stack.pop() # 꼬리 제거
        world[dy][dx] = 0
    
    world[y][x] = 1 # 지도에 기록